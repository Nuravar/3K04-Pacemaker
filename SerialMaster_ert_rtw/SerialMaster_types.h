/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: SerialMaster_types.h
 *
 * Code generated for Simulink model 'SerialMaster'.
 *
 * Model version                  : 1.29
 * Simulink Coder version         : 23.2 (R2023b) 01-Aug-2023
 * C/C++ source code generated on : Sun Nov 26 16:21:28 2023
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#ifndef RTW_HEADER_SerialMaster_types_h_
#define RTW_HEADER_SerialMaster_types_h_
#include "rtwtypes.h"
#include "MW_SVD.h"

/* Custom Type definition for MATLABSystem: '<S5>/Serial Transmit1' */
#include "MW_SVD.h"
#ifndef struct_tag_0QIIqIWUIOhUbf1p9QN9pB
#define struct_tag_0QIIqIWUIOhUbf1p9QN9pB

struct tag_0QIIqIWUIOhUbf1p9QN9pB
{
  int32_T __dummy;
};

#endif                                 /* struct_tag_0QIIqIWUIOhUbf1p9QN9pB */

#ifndef typedef_b_freedomk64f_Hardware_Serial_T
#define typedef_b_freedomk64f_Hardware_Serial_T

typedef struct tag_0QIIqIWUIOhUbf1p9QN9pB b_freedomk64f_Hardware_Serial_T;

#endif                             /* typedef_b_freedomk64f_Hardware_Serial_T */

#ifndef struct_tag_GV9UedAE1zOVNNbkXknChB
#define struct_tag_GV9UedAE1zOVNNbkXknChB

struct tag_GV9UedAE1zOVNNbkXknChB
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_Serial_T Hw;
  MW_Handle_Type MW_SCIHANDLE;
};

#endif                                 /* struct_tag_GV9UedAE1zOVNNbkXknChB */

#ifndef typedef_freedomk64f_SCIWrite_SerialMa_T
#define typedef_freedomk64f_SCIWrite_SerialMa_T

typedef struct tag_GV9UedAE1zOVNNbkXknChB freedomk64f_SCIWrite_SerialMa_T;

#endif                             /* typedef_freedomk64f_SCIWrite_SerialMa_T */

#ifndef struct_tag_CWH6DTHP01Gd55CkkzwSIG
#define struct_tag_CWH6DTHP01Gd55CkkzwSIG

struct tag_CWH6DTHP01Gd55CkkzwSIG
{
  int32_T isInitialized;
  boolean_T isSetupComplete;
  real_T pCumSum;
  real_T pCumSumRev[299];
  real_T pCumRevIndex;
  real_T pModValueRev;
};

#endif                                 /* struct_tag_CWH6DTHP01Gd55CkkzwSIG */

#ifndef typedef_h_dsp_internal_SlidingWindowA_T
#define typedef_h_dsp_internal_SlidingWindowA_T

typedef struct tag_CWH6DTHP01Gd55CkkzwSIG h_dsp_internal_SlidingWindowA_T;

#endif                             /* typedef_h_dsp_internal_SlidingWindowA_T */

#ifndef struct_tag_BlgwLpgj2bjudmbmVKWwDE
#define struct_tag_BlgwLpgj2bjudmbmVKWwDE

struct tag_BlgwLpgj2bjudmbmVKWwDE
{
  uint32_T f1[8];
};

#endif                                 /* struct_tag_BlgwLpgj2bjudmbmVKWwDE */

#ifndef typedef_cell_wrap_SerialMaster_T
#define typedef_cell_wrap_SerialMaster_T

typedef struct tag_BlgwLpgj2bjudmbmVKWwDE cell_wrap_SerialMaster_T;

#endif                                 /* typedef_cell_wrap_SerialMaster_T */

#ifndef struct_tag_bpXjadQgrd0jNiqC0SXNYB
#define struct_tag_bpXjadQgrd0jNiqC0SXNYB

struct tag_bpXjadQgrd0jNiqC0SXNYB
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  boolean_T TunablePropsChanged;
  cell_wrap_SerialMaster_T inputVarSize;
  h_dsp_internal_SlidingWindowA_T *pStatistic;
  int32_T NumChannels;
  int32_T FrameLength;
  h_dsp_internal_SlidingWindowA_T _pobj0;
};

#endif                                 /* struct_tag_bpXjadQgrd0jNiqC0SXNYB */

#ifndef typedef_dsp_simulink_MovingAverage_Se_T
#define typedef_dsp_simulink_MovingAverage_Se_T

typedef struct tag_bpXjadQgrd0jNiqC0SXNYB dsp_simulink_MovingAverage_Se_T;

#endif                             /* typedef_dsp_simulink_MovingAverage_Se_T */

#ifndef struct_tag_EkIWEs70Gs0LyfeXELZ2TC
#define struct_tag_EkIWEs70Gs0LyfeXELZ2TC

struct tag_EkIWEs70Gs0LyfeXELZ2TC
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_Serial_T Hw;
  MW_Handle_Type MW_DIGITALIO_HANDLE;
};

#endif                                 /* struct_tag_EkIWEs70Gs0LyfeXELZ2TC */

#ifndef typedef_freedomk64f_DigitalWrite_Seri_T
#define typedef_freedomk64f_DigitalWrite_Seri_T

typedef struct tag_EkIWEs70Gs0LyfeXELZ2TC freedomk64f_DigitalWrite_Seri_T;

#endif                             /* typedef_freedomk64f_DigitalWrite_Seri_T */

#ifndef struct_tag_RYgVoAXTz61tXGMaBAGv7F
#define struct_tag_RYgVoAXTz61tXGMaBAGv7F

struct tag_RYgVoAXTz61tXGMaBAGv7F
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_Serial_T Hw;
  MW_Handle_Type MW_PWM_HANDLE;
};

#endif                                 /* struct_tag_RYgVoAXTz61tXGMaBAGv7F */

#ifndef typedef_freedomk64f_PWMOutput_SerialM_T
#define typedef_freedomk64f_PWMOutput_SerialM_T

typedef struct tag_RYgVoAXTz61tXGMaBAGv7F freedomk64f_PWMOutput_SerialM_T;

#endif                             /* typedef_freedomk64f_PWMOutput_SerialM_T */

#ifndef struct_tag_s1eQZAg8cMgwN6kxxyzYvC
#define struct_tag_s1eQZAg8cMgwN6kxxyzYvC

struct tag_s1eQZAg8cMgwN6kxxyzYvC
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_Serial_T Hw;
  MW_Handle_Type MW_ANALOGIN_HANDLE;
  real_T SampleTime;
};

#endif                                 /* struct_tag_s1eQZAg8cMgwN6kxxyzYvC */

#ifndef typedef_freedomk64f_AnalogInput_Seria_T
#define typedef_freedomk64f_AnalogInput_Seria_T

typedef struct tag_s1eQZAg8cMgwN6kxxyzYvC freedomk64f_AnalogInput_Seria_T;

#endif                             /* typedef_freedomk64f_AnalogInput_Seria_T */

#ifndef struct_tag_q6HQSF2nXq6EjCNj0vbuLD
#define struct_tag_q6HQSF2nXq6EjCNj0vbuLD

struct tag_q6HQSF2nXq6EjCNj0vbuLD
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_Serial_T Hw;
  MW_Handle_Type MW_DIGITALIO_HANDLE;
  real_T SampleTime;
};

#endif                                 /* struct_tag_q6HQSF2nXq6EjCNj0vbuLD */

#ifndef typedef_freedomk64f_DigitalRead_Seria_T
#define typedef_freedomk64f_DigitalRead_Seria_T

typedef struct tag_q6HQSF2nXq6EjCNj0vbuLD freedomk64f_DigitalRead_Seria_T;

#endif                             /* typedef_freedomk64f_DigitalRead_Seria_T */

#ifndef struct_tag_214cR1nKZWaoqoq0FTtOUH
#define struct_tag_214cR1nKZWaoqoq0FTtOUH

struct tag_214cR1nKZWaoqoq0FTtOUH
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  b_freedomk64f_Hardware_Serial_T Hw;
  MW_Handle_Type MW_SCIHANDLE;
  real_T SampleTime;
};

#endif                                 /* struct_tag_214cR1nKZWaoqoq0FTtOUH */

#ifndef typedef_freedomk64f_SCIRead_SerialMas_T
#define typedef_freedomk64f_SCIRead_SerialMas_T

typedef struct tag_214cR1nKZWaoqoq0FTtOUH freedomk64f_SCIRead_SerialMas_T;

#endif                             /* typedef_freedomk64f_SCIRead_SerialMas_T */

#ifndef struct_tag_O0UAiliRyLLAe38ibfdAhE
#define struct_tag_O0UAiliRyLLAe38ibfdAhE

struct tag_O0UAiliRyLLAe38ibfdAhE
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  b_freedomk64f_Hardware_Serial_T Hw;
  uint32_T BusSpeed;
  MW_Handle_Type MW_I2C_HANDLE;
};

#endif                                 /* struct_tag_O0UAiliRyLLAe38ibfdAhE */

#ifndef typedef_b_freedomk64f_I2CMasterWrite__T
#define typedef_b_freedomk64f_I2CMasterWrite__T

typedef struct tag_O0UAiliRyLLAe38ibfdAhE b_freedomk64f_I2CMasterWrite__T;

#endif                             /* typedef_b_freedomk64f_I2CMasterWrite__T */

#ifndef struct_tag_v5Zyp5raUQrCF4f9Ln2EwE
#define struct_tag_v5Zyp5raUQrCF4f9Ln2EwE

struct tag_v5Zyp5raUQrCF4f9Ln2EwE
{
  boolean_T matlabCodegenIsDeleted;
  int32_T isInitialized;
  boolean_T isSetupComplete;
  real_T SampleTime;
  b_freedomk64f_I2CMasterWrite__T i2cobj;
};

#endif                                 /* struct_tag_v5Zyp5raUQrCF4f9Ln2EwE */

#ifndef typedef_freedomk64f_fxos8700_SerialMa_T
#define typedef_freedomk64f_fxos8700_SerialMa_T

typedef struct tag_v5Zyp5raUQrCF4f9Ln2EwE freedomk64f_fxos8700_SerialMa_T;

#endif                             /* typedef_freedomk64f_fxos8700_SerialMa_T */

/* Parameters (default storage) */
typedef struct P_SerialMaster_T_ P_SerialMaster_T;

/* Forward declaration for rtModel */
typedef struct tag_RTM_SerialMaster_T RT_MODEL_SerialMaster_T;

#endif                                 /* RTW_HEADER_SerialMaster_types_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
