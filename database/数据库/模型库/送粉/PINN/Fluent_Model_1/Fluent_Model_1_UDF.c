#include "udf.h"

#include "sg_mphase.h" 

#include "sg_mem.h"

/* Level-set model */

extern FLUENT_EXPORT cxboolean LSF_Front_Recon_P;
extern FLUENT_EXPORT cxboolean LSF_Front_Area_Compute_P;

extern FLUENT_EXPORT void Domain_LSF_Signed_Distance(Domain *domain, Svar sv_lsf);
extern FLUENT_EXPORT int Create_Tree(Domain *domain);
extern FLUENT_EXPORT void Free_Tree(Domain *domain);
extern FLUENT_EXPORT void Recon_LSF_Front(Domain *phaseDomain);
extern FLUENT_EXPORT void LSF_PreProcessing(Domain *domain);
extern FLUENT_EXPORT void LSF_PostProcessing(Domain *domain);
extern FLUENT_EXPORT real get_surface_distance_scaled(cell_t c, Thread *t);
extern FLUENT_EXPORT void LSF_Surface_Tension(Domain *mdomain, Svar sv_lsf);
extern FLUENT_EXPORT void LSF_Derivatives(Domain *mdomain);

#define C_LSF(c,t) C_STORAGE_R(c,t,SV_LSF)
#define F_LSF C_LSF

#define C_LSF_G(c,t)  C_STORAGE_R_NV(c,t,SV_LSF_G)
#define C_LSF_RG(c,t) C_STORAGE_R_NV(c,t,SV_LSF_RG)
#define C_LSF_M1(c,t) C_STORAGE_R(c,t,SV_LSF_M1)
#define C_LSF_M2(c,t) C_STORAGE_R(c,t,SV_LSF_M2)
#define C_LSF_AP(c,t) C_STORAGE_R(c,t,SV_LSF_AP)
#define C_LSF_S(c,t)  C_STORAGE_R(c,t,SV_LSF_S)
#define C_LSF_M1_0(c,t) C_STORAGE_R(c,t,SV_LSF_M1_0)

#define LSF_BC_FLUX 0
#define LSF_BC_VALUE 1

/* Use UDS0 as SV_LS temporarily until SV_LS equation established */
/*#define SV_LS SV_UDS_I(0)
#define SV_LS_M1 SV_UDSI_M1(0)
#define SV_LS_M2 SV_UDSI_M2(0)
#define SV_LS_RG SV_UDSI_RG(0)
#define SV_LS_G SV_UDSI_G(0)*/

/* end of temporary */
/*typedef real realGeo;*/

void Model_Initialize_lsf(void);
cxboolean if_lsf(void);
cxboolean if_lsf_on_domain(Domain *d);

#if RP_POLYHEDRA && RP_3D
extern FLUENT_EXPORT cxboolean use_polyhedral;

typedef struct polycell_struct
{
    real (*r_n)[ND_ND];    /* node coordinates */
    real (*farea)[ND_ND];  /* face area vectors */
    real *fxmin;           /* min x of each face */
    real *fxmax;           /* max x of each face */
    real (*edges)[ND_ND];  /* used in find_cut_volume */
    int *faces;               /* face->node connectivity */
    int *face_nnodes;         /* no. of nodes per face */
    int nfaces;               /* no. of faces */
    int nnodes;               /* no. of nodes */
    int max_nodes_per_face;   /* max. no. of nodes in a face of cell */
    int memory_allocated;     /* length of char memory allocated */
} PolyCell;

extern FLUENT_EXPORT void free_polycell(PolyCell *pc);
extern FLUENT_EXPORT real get_surface_distance_scaled_polyhedra(PolyCell *pc, cell_t c, Thread *t);
extern FLUENT_EXPORT void init_polycell(PolyCell *pc);

#endif /* RP_POLYHEDRA && RP_3D */

#define DEBUG_LSF 0
#define LSF_DEBUG_AREA 0

typedef enum /* used in facet area compute via get_intersection_facet in vof_dist.c */
{
  LINE_FACET_2D = 0,
  AXI_FACET_2D = 1,
  POLYGON_FACET_3D = 2
} LSF_Facet_Type;





#define PI 3.1415926

#define sigma_q 0.22	/*the absorption rate 0.1465 the original*/

#define P 2000 	/*Power W*/

#define R 0.00170	/*the equivalent radius of the laser spot m*/

#define ks 40		/*thermal conductivity solid Wm-1K-1*/

#define kl 200	/*effective thermal conductivity liquid Wm-1K-1*/

#define Cp 750		/*average thermal capacity*/

#define Ts 1626	/*temperature of solidus T15 K*/

#define Tl 1653	/*temperature of liquidus T15 K*/

#define Tsst 1690	/*temperature of solidus 42crmo K*/

#define Tlst 1730	/*temperature of liquidus 42crmo K*/

/*#define v 0.5		scanning speed m/min*/

#define Vs 0.007	/*scanning speed m/s*/

#define hm 0.05e-3	/*the thickness of the mass source input*/

#define h 0.05e-3	/*the thickness of the energy source input m*/

#define ori 0.0020  		/*the x coordinate where start the laser */

#define A 0.0000015	/*the crosssection area of actual...*/

#define Lh	250000		/*the latent heat of the material*/

#define lamdam 3.0		/*the distribution coefficient of mass*/

#define lamdae 3.0		/*the distribution coefficient of energy*/

#define pm 7780	 /*density*/

/*#define Vf 0.025	feeding rate m/s*/

/*#define D 0.0012	the diameter of the metal wire*/

#define rr 0.0008	/*the equivalent radius of the diameter*/

/*#define aa 0.85	the coefficient to adjust total energy input */

#define t15_index 0

#define track 0.0018  /*center of the second track */


//  for the smaller mesh scale, single sym track


DEFINE_INIT(phase_init_func, mixture_domain)

{

	int phase_domain_index;

	cell_t cell;

	Thread *cell_thread;

	Domain *subdomain;

	real xc[ND_ND];
	/* loop over all subdomains (phases) in the superdomain (mixture) */

	sub_domain_loop(subdomain, mixture_domain, phase_domain_index)

	{
	/* loop if secondary phase */

		if (DOMAIN_ID(subdomain) == 3)

		/* loop over all cell threads in the secondary phase domain */

		thread_loop_c (cell_thread,subdomain)

		{
		/* loop over all cells in secondary phase cell threads */

			begin_c_loop_all (cell,cell_thread)

			{

				C_CENTROID(xc,cell,cell_thread);

				if (xc[2]>0)

					/* set volume fraction to 1 for centroid */
					

					C_VOF(cell,cell_thread) = 1.; 
				else

					/* otherwise initialize to zero */

					C_VOF(cell,cell_thread) = 0.;

			}

			end_c_loop_all (cell,cell_thread)

		}

		else if (DOMAIN_ID(subdomain) == 2)

		/* loop over all cell threads in the primary phase domain */

		thread_loop_c (cell_thread,subdomain)

		{
		/* loop over all cells in primary phase cell threads */

			begin_c_loop_all (cell,cell_thread)

			{

				C_CENTROID(xc,cell,cell_thread);

				if (xc[2]<0)

					/* set species mass fraction to 1 for centroid */
					C_YI(cell,cell_thread,t15_index)=0;
					/* set volume fraction to 1 for centroid */
					C_VOF(cell,cell_thread) = 1.; 

				if(xc[2]>0)

					/* otherwise initialize to zero */

					C_VOF(cell,cell_thread) = 0.;
				
			}

			end_c_loop_all (cell,cell_thread)

		}
	}

}

DEFINE_INIT(temp_init_func,d)
{
  cell_t c;
  Thread *t;
  real xc[ND_ND];

  /* loop over all cell threads in the domain  */
  thread_loop_c(t,d)
    {

      /* loop over all cells  */
      begin_c_loop_all(c,t)
        {
          C_CENTROID(xc,c,t);
          if (sqrt(pow(xc[0]+ori,2)+pow(xc[1],2))<rr && xc[2]<0 && xc[2]>-0.0001)
            C_T(c,t) = 1730.;
          else
            C_T(c,t) = 300.;
        }
      end_c_loop_all(c,t)
    }
}

DEFINE_INIT(liqf_init_func,mixture_domain)
{
	cell_t c;

	Thread *t;

	real xc[ND_ND];

	int phase_domain_index;

	Domain *subdomain;

	/* loop over all subdomains (phases) in the superdomain (mixture) */

	sub_domain_loop(subdomain, mixture_domain, phase_domain_index)

	{
	/* loop if primary phase */

		if (DOMAIN_ID(subdomain) == 2)
  
		 /* loop over all cell threads in the domain  */

		thread_loop_c(t,subdomain)
		{

			/* loop over all cells  */
			 begin_c_loop_all(c,t)
				 {
					  C_CENTROID(xc,c,t);
					  if (sqrt(pow(xc[0]+ori,2)+pow(xc[1],2))<rr && xc[2]<0 && xc[2]>-0.0001)
						C_LIQF(c,t) = 1.;
					
				}
			end_c_loop_all(c,t)
		}
	}
}




DEFINE_PROPERTY(surface_tension,c,t)

{

    real x[ND_ND],st;

	real tempp = C_T(c,t);

	//if(tempp >= Ts && tempp<Ts+300)

	//  st=1+0.00125*(tempp-Ts);	/* surface tension when liquid N/m */

	//else if(tempp>=Ts+300 &&tempp<Ts+500)

	//  st=1.375-0.001875*(tempp-Ts-300);

	if(tempp >= Ts)

		st=-0.40965+0.0011508*tempp ;

	else
		st=1.461551;	/* surface tension when solid N/m */

	return st;

}



DEFINE_PROPERTY(cell_conduct_t15,c,t)

{

    real km;	/*conductivity*/

    real tempp = C_T(c,t);	/*temperature*/

    if (tempp >= Tl)

      km = kl;

    else if (tempp > Ts && tempp < Tl)

      km = 1.0/(1.0/ks+(tempp-Ts)*(1.0/kl-1.0/ks)/(Tl-Ts));

    else

      km = ks;

    return km;

}

DEFINE_PROPERTY(cell_conduct_42crmo,c,t)

{

    real km;	/*conductivity*/

    real tempp = C_T(c,t);	/*temperature*/

    if (tempp >= Tlst)

      km = kl;

    else if (tempp > Tsst && tempp < Tlst)

      km = 1.0/(1.0/ks+(tempp-Tsst)*(1.0/kl-1.0/ks)/(Tlst-Tsst));

    else

      km = ks;

    return km;

}





DEFINE_SOURCE(energy_source, c, t, dS, eqn)

{

	real source,x[ND_ND],r, vol,vol1,time,f,M,g,q;

	time=RP_Get_Real("flow-time");

	C_CENTROID(x,c,t); 	/*find the centroid of cell c,store the coordinates in the x array*/

	f = C_LSF(c,t);		/*access level-set function*/

	g = fabs(C_LSF_G(c,t)[2]);

	q=f/g;

	r = sqrt(pow((x[0] + ori - Vs * time), 2.0) + pow(x[1], 2.0));

	if (r < R && q >= 0 && q < h) { //first layer, laser energy

		vol = lamdae * r*r / (R*R);

		source = lamdae * sigma_q * P * exp(-vol) / (h*PI*R*R) / (1 - exp(-lamdae)) ;
	//}
	//else if (r <= rr - 0.0002 && q >= hm && q < 2 * hm) { // second layer in the middle, melting powder energy(compared to the upper, second condition is wiped?)

		//vol = lamdam * r*r / (rr*rr);

		//M = lamdam * pm*A*Vs * exp(-vol) / (PI*rr*rr) / (1 - exp(-lamdam));

		//source = (Cp*(Tl - 300) + Lh)*M / hm;
	//}
	}
	else if (r <= rr - 0.0002 && q >= hm && q < 2 * hm) { // second layer in the middle, melting powder energy(compared to the upper, second condition is wiped?)

		vol = lamdam * r*r / (rr*rr);

		M = lamdam * pm*A*Vs * exp(-vol) / (PI*rr*rr) / (1 - exp(-lamdam));

		source = (Cp*(Tl - 300) + Lh)*M / hm;
	}
	else
		source = 0.;


	dS[eqn]=0.0;

	return source;

}



DEFINE_SOURCE(mass_source,c,t,dS,eqn) 

{

	Thread *mixture_thread;

	real source,x[ND_ND],vol,time,r, M,f,g,q;

	time=RP_Get_Real("flow-time");

	if (time<=4e-5)  
	{
		source = 0.0;

		dS[eqn] = 0.0;

		return source;
	}
	
	else {

		C_CENTROID(x, c, t);

		mixture_thread = THREAD_SUPER_THREAD(t);  
		//because this udf is assigned in cell zone -- mixture part, we need to get the super thread first.

		f = C_LSF(c, mixture_thread);		/*access level-set function*/

		//g = C_LSF_RG(c,mixture_thread)[2];
		g = fabs(C_LSF_G(c, mixture_thread)[2]);

		q = f / g;

		r = sqrt(pow((x[0] + ori - Vs * time), 2.0) + pow(x[1], 2.0));

		if ((r <= rr - 0.0002 && q >= hm && q < 2 * hm) || (r <= rr && r > rr - 0.0002 && q >= 0 && q < hm))
		{

			vol = lamdam * r*r / (rr*rr);

			source = lamdam * pm*A*Vs*exp(-vol) / (PI*rr*rr*hm) / (1 - exp(-lamdam));

		}
		else {
			source = 0.0;
		}

	}

	dS[eqn]= 0.0; 

	return source; 
}

/*
DEFINE_ADJUST(adjust_coolingrate, domain)
{
	Thread *t;
	cell_t c;
	//face_t f;
	//double a;

	domain =Get_Domain(1);//operate on the phase1

	thread_loop_c(t,domain)
	{
		//Cooling rate
		if (NULL != THREAD_STORAGE(t,SV_UDS_I(0)))
		{
			begin_c_loop(c,t)
			{
				C_UDSI(c,t,0) = (C_T(c,t)-C_T_M1(c,t))*50000;
			
		    //NV_MAG() get the magnitude of the vector,NV_MAG2() get square
			}
			end_c_loop(c,t)
		}
		//R=C/G
		if (NULL != THREAD_STORAGE(t,SV_UDS_I(1)))
		{
			begin_c_loop(c,t)
			{
				//C_UDSI(c,t,1)=6000000/3000000;
				//a=NV_MAG(C_T_RG(c,t));

				C_UDSI(c,t,1) =C_T(c,t);
			}
			end_c_loop(c,t)
		}
		
		//G/R=G^2/C
		if (NULL != THREAD_STORAGE(t,SV_UDS_I(2)))
		{
			begin_c_loop(c,t)
			{
				C_UDSI(c,t,2)=C_T_RG(c,t)[0];
			//C_UDSI(c,t,2) = NV_MAG2(C_T_RG(c,t))/C_UDSI(c,t,0);
			}
			end_c_loop(c,t)
		}
	}
}
*/



DEFINE_ON_DEMAND(store_gradient)
{ 
	
	
	Domain *domain;
	cell_t c;
	Thread *t;
	domain=Get_Domain(2);
	
	/* Fill the UDM with magnitude of gradient. */
	thread_loop_c (t,domain)
	{
		begin_c_loop (c,t)
		{
			C_UDMI(c,t,0) = NV_MAG(C_T_RG(c,t));
			
		}
		end_c_loop (c,t)
	}
}

DEFINE_ON_DEMAND(mushyfilter)
{ 
	Domain *domain;
	cell_t c;
	Thread *t;
	domain=Get_Domain(2);
	
	/* Fill the UDM with mushyzone symbol. */
	thread_loop_c (t,domain)
	{
		begin_c_loop (c,t)
		{
			C_UDMI(c,t,1) = (C_T(c,t)-C_T_M1(c,t))*50000;

			if (C_T(c,t)<Tlst-50 && C_T(c,t)>Ts-100)
			{
				C_UDMI(c,t,2) = 1;
			}
			else
			{
				C_UDMI(c,t,2)=0;
			}
		}
		end_c_loop (c,t)
	}
}

DEFINE_ON_DEMAND(phasefilter)
{ 
	Domain *domain;
	cell_t c;
	Thread *t;
	domain=Get_Domain(1);
	/* Fill the UDM with mushyzone symbol. */
	thread_loop_c (t,domain)
	{
		begin_c_loop (c,t)
		{
			if (C_LSF(c,t)>0.0001)
			{
				C_UDMI(c,t,3) = 1;
			}
			else
			{
				C_UDMI(c,t,3)=0;
			}
		}
		end_c_loop (c,t)
	}
}

DEFINE_ON_DEMAND(coolingfilter)
{ 
	Domain *domain;
	cell_t c;
	Thread *t;
	domain=Get_Domain(2);
	/* Fill the UDM with mushyzone symbol. */
	thread_loop_c (t,domain)
	{
		begin_c_loop (c,t)
		{
			if (C_UDMI(c,t,1)<0)
			{
				C_UDMI(c,t,4)=C_UDMI(c,t,1)-10;
			}
			else
			{
				C_UDMI(c,t,4)=C_UDMI(c,t,1)+10;
			}
		}
		end_c_loop (c,t)
	}
}

/*
DEFINE_ON_DEMAND(positionfilter)
{ 
	Domain *domain;
	cell_t c;
	Thread *t;
	domain=Get_Domain(2);
	time=RP_Get_Real("flow-time");
	real x[ND_ND];
	thread_loop_c (t,domain)
	{
		begin_c_loop (c,t)
		{   
			C_CENCROID(x,c,t);
			if (x[0]<ori+Vs*time)
			{
				C_UDMI(c,t,5)=1;
			}
			else
			{
				C_UDMI(c,t,5)=0;
			}
		}
		end_c_loop (c,t)
	}
}
*/