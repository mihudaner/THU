      SUBROUTINE DFLUX(FLUX,SOL,KSTEP,KINC,TIME,NOEL,NPT,COORDS,JLTYP,
     1                 TEMP,PRESS,SNAME)
C
      INCLUDE 'ABA_PARAM.INC'
      DIMENSION COORDS(3),FLUX(2),TIME(2)
      CHARACTER*80 SNAME


	v=5
	d1=v*TIME(2)

C
	x=COORDS(1)
	y=COORDS(2)
	z=COORDS(3)
C     a,b,c为椭球的半轴
	a=6.5
	b=6.5
	c=0.36
	PI=3.1415
	
	x0=5
	y0=0
	z0=0.45
        Q=2000000

       IF (KSTEP .LE. 51) THEN
        shape=exp(-3*(x-x0-d1)**2/a**2-3*(y-y0)**2/b**2-3*(z-z0)**2/c**2)
       ELSE
        shape=0
       ENDIF
        heat=6*sqrt(3.0)*Q/(a*b*c*PI*sqrt(PI))

C     JLTYP＝1，表示为体热源
	JLTYP=1
        FLUX(1)=heat*shape
      RETURN
      END
