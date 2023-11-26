/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: SerialMaster.h
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

#ifndef RTW_HEADER_SerialMaster_h_
#define RTW_HEADER_SerialMaster_h_
#ifndef SerialMaster_COMMON_INCLUDES_
#define SerialMaster_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_digitalIO.h"
#include "MW_PWM.h"
#include "MW_AnalogIn.h"
#include "MW_SCI.h"
#include "MW_I2C.h"
#endif                                 /* SerialMaster_COMMON_INCLUDES_ */

#include "SerialMaster_types.h"
#include "send_DCM.h"
#include <stddef.h>

/* Macros for accessing real-time model data structure */
#ifndef rtmGetErrorStatus
#define rtmGetErrorStatus(rtm)         ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
#define rtmSetErrorStatus(rtm, val)    ((rtm)->errorStatus = (val))
#endif

/* Block signals (default storage) */
typedef struct {
  real_T csumrev[299];
  uint8_T RxData[20];
  uint8_T RxDataLocChar[20];
  real_T D2_PACE_CHARGE_CTRL;          /* '<Root>/PACEMAKER STATEFLOW' */
  real_T D3_VENT_CMP_REF_PWM;          /* '<Root>/PACEMAKER STATEFLOW' */
  real_T D4_Z_ATR_CTRL;                /* '<Root>/PACEMAKER STATEFLOW' */
  real_T D5_PACING_REF_PWM;            /* '<Root>/PACEMAKER STATEFLOW' */
  real_T D6_ATR_CMP_REF_PWM;           /* '<Root>/PACEMAKER STATEFLOW' */
  real_T D7_Z_VENT_CTRL;               /* '<Root>/PACEMAKER STATEFLOW' */
  real_T D8_ATR_PACE_CTRL;             /* '<Root>/PACEMAKER STATEFLOW' */
  real_T D9_VENT_PACE_CTRL;            /* '<Root>/PACEMAKER STATEFLOW' */
  real_T D10_PACE_GND_CTRL;            /* '<Root>/PACEMAKER STATEFLOW' */
  real_T D11_ATR_GND_CTRL;             /* '<Root>/PACEMAKER STATEFLOW' */
  real_T D12_VENT_GND_CTRL;            /* '<Root>/PACEMAKER STATEFLOW' */
  real_T rtb_u_m;
  real_T modValueRev;
  real_T z;
  real_T CastToDouble14;               /* '<S2>/Cast To Double14' */
  real_T Multiply3;
  real_T Product;
  real_T Multiply7;
  real_T Multiply4;
  real_T Multiply8;
  real_T Product1;
  real_T rtb_FXOS87006AxesSensor1_idx_0;
  real_T rtb_FXOS87006AxesSensor1_idx_1;
  int16_T b_RegisterValue[3];
  real32_T Gain;                       /* '<S2>/Gain' */
  real32_T Gain1;                      /* '<S2>/Gain1' */
  real32_T TmpLatchAtATRSignalOutport1;
  real32_T TmpLatchAtVENTSignalOutport1;
  uint8_T BytePack[4];                 /* '<S5>/Byte Pack' */
  uint8_T BytePack1[4];                /* '<S5>/Byte Pack1' */
  uint8_T Mode;                        /* '<S2>/Chart2' */
  uint8_T LRL;                         /* '<S2>/Chart2' */
  uint8_T URL;                         /* '<S2>/Chart2' */
  uint8_T MSR;                         /* '<S2>/Chart2' */
  uint8_T AVDelay;                     /* '<S2>/Chart2' */
  uint8_T AAmp;                        /* '<S2>/Chart2' */
  uint8_T VAmp;                        /* '<S2>/Chart2' */
  uint8_T APulseWidth;                 /* '<S2>/Chart2' */
  uint8_T VPulseWidth;                 /* '<S2>/Chart2' */
  uint8_T ASensitivity;                /* '<S2>/Chart2' */
  uint8_T VSensitivity;                /* '<S2>/Chart2' */
  uint8_T ARP;                         /* '<S2>/Chart2' */
  uint8_T VRP;                         /* '<S2>/Chart2' */
  uint8_T PVARP;                       /* '<S2>/Chart2' */
  uint8_T ActivityThreshold;           /* '<S2>/Chart2' */
  uint8_T ReactionTime;                /* '<S2>/Chart2' */
  uint8_T ResponseFactor;              /* '<S2>/Chart2' */
  uint8_T RecoveryTime;                /* '<S2>/Chart2' */
  boolean_T D13_FRONTEND_CONTROL;      /* '<Root>/PACEMAKER STATEFLOW' */
  boolean_T GreenLED;                  /* '<S2>/Chart2' */
} B_SerialMaster_T;

/* Block states (default storage) for system '<Root>' */
typedef struct {
  dsp_simulink_MovingAverage_Se_T obj; /* '<S4>/ ' */
  freedomk64f_fxos8700_SerialMa_T obj_k;/* '<S4>/FXOS8700 6-Axes Sensor1' */
  freedomk64f_AnalogInput_Seria_T obj_j;/* '<S2>/VentSignalIn' */
  freedomk64f_AnalogInput_Seria_T obj_i;/* '<S2>/AtrSignalIn' */
  freedomk64f_DigitalRead_Seria_T obj_b;/* '<S2>/Digital Read1' */
  freedomk64f_DigitalRead_Seria_T obj_c;/* '<S2>/Digital Read' */
  freedomk64f_SCIRead_SerialMas_T obj_k3;/* '<S2>/Serial Receive1' */
  freedomk64f_DigitalWrite_Seri_T obj_e;/* '<S2>/Digital Write' */
  freedomk64f_DigitalWrite_Seri_T obj_kk;/* '<S1>/Digital Write9' */
  freedomk64f_DigitalWrite_Seri_T obj_h;/* '<S1>/Digital Write8' */
  freedomk64f_DigitalWrite_Seri_T obj_d;/* '<S1>/Digital Write7' */
  freedomk64f_DigitalWrite_Seri_T obj_hx;/* '<S1>/Digital Write6' */
  freedomk64f_DigitalWrite_Seri_T obj_g;/* '<S1>/Digital Write5' */
  freedomk64f_DigitalWrite_Seri_T obj_n;/* '<S1>/Digital Write4' */
  freedomk64f_DigitalWrite_Seri_T obj_f;/* '<S1>/Digital Write2' */
  freedomk64f_DigitalWrite_Seri_T obj_a;/* '<S1>/Digital Write11' */
  freedomk64f_DigitalWrite_Seri_T obj_cw;/* '<S1>/Digital Write10' */
  freedomk64f_PWMOutput_SerialM_T obj_ng;/* '<S1>/PWM Output2' */
  freedomk64f_PWMOutput_SerialM_T obj_nz;/* '<S1>/PWM Output1' */
  freedomk64f_PWMOutput_SerialM_T obj_hj;/* '<S1>/PWM Output' */
  freedomk64f_SCIWrite_SerialMa_T obj_o;/* '<S5>/Serial Transmit1' */
  real_T UnitDelay_DSTATE;             /* '<S4>/Unit Delay' */
  real_T Standby_Period;               /* '<Root>/PACEMAKER STATEFLOW' */
  uint32_T temporalCounter_i1;         /* '<Root>/PACEMAKER STATEFLOW' */
  uint8_T is_active_c3_SerialMaster;   /* '<Root>/PACEMAKER STATEFLOW' */
  uint8_T is_c3_SerialMaster;          /* '<Root>/PACEMAKER STATEFLOW' */
  uint8_T is_AAI;                      /* '<Root>/PACEMAKER STATEFLOW' */
  uint8_T is_AOO;                      /* '<Root>/PACEMAKER STATEFLOW' */
  uint8_T is_VOO;                      /* '<Root>/PACEMAKER STATEFLOW' */
  uint8_T is_VVI;                      /* '<Root>/PACEMAKER STATEFLOW' */
  uint8_T FUNC;                        /* '<S2>/Chart2' */
  uint8_T SYNC;                        /* '<S2>/Chart2' */
  uint8_T LRLIN;                       /* '<S2>/Chart2' */
  uint8_T MSRIN;                       /* '<S2>/Chart2' */
  uint8_T URLIN;                       /* '<S2>/Chart2' */
  uint8_T AAmpIN;                      /* '<S2>/Chart2' */
  uint8_T AVDelayIN;                   /* '<S2>/Chart2' */
  uint8_T ARPIN;                       /* '<S2>/Chart2' */
  uint8_T APulseWidthIN;               /* '<S2>/Chart2' */
  uint8_T ASensitivityIN;              /* '<S2>/Chart2' */
  uint8_T ActivityThresholdIN;         /* '<S2>/Chart2' */
  uint8_T MODEIN;                      /* '<S2>/Chart2' */
  uint8_T PVARPIN;                     /* '<S2>/Chart2' */
  uint8_T ReactionTimeIN;              /* '<S2>/Chart2' */
  uint8_T RecoveryTimeIN;              /* '<S2>/Chart2' */
  uint8_T ResponseFactorIN;            /* '<S2>/Chart2' */
  uint8_T VAmpIN;                      /* '<S2>/Chart2' */
  uint8_T VPulseWidthIN;               /* '<S2>/Chart2' */
  uint8_T VRPIN;                       /* '<S2>/Chart2' */
  uint8_T VSensitivityIN;              /* '<S2>/Chart2' */
  uint8_T is_active_c4_SerialMaster;   /* '<S2>/Chart2' */
  uint8_T is_c4_SerialMaster;          /* '<S2>/Chart2' */
  uint8_T temporalCounter_i1_f;        /* '<S2>/Chart2' */
} DW_SerialMaster_T;

/* Parameters (default storage) */
struct P_SerialMaster_T_ {
  real_T AtrSignalIn_SampleTime;       /* Expression: SampleTime
                                        * Referenced by: '<S2>/AtrSignalIn'
                                        */
  real_T DigitalRead_SampleTime;       /* Expression: SampleTime
                                        * Referenced by: '<S2>/Digital Read'
                                        */
  real_T DigitalRead1_SampleTime;      /* Expression: SampleTime
                                        * Referenced by: '<S2>/Digital Read1'
                                        */
  real_T SerialReceive1_SampleTime;    /* Expression: -1
                                        * Referenced by: '<S2>/Serial Receive1'
                                        */
  real_T VentSignalIn_SampleTime;      /* Expression: SampleTime
                                        * Referenced by: '<S2>/VentSignalIn'
                                        */
  real_T Constant_Value;               /* Expression: 1
                                        * Referenced by: '<S5>/Constant'
                                        */
  real_T FXOS87006AxesSensor1_SampleTime;/* Expression: -1
                                          * Referenced by: '<S4>/FXOS8700 6-Axes Sensor1'
                                          */
  real_T Multiply3_Gain;               /* Expression: 0.01
                                        * Referenced by: '<S2>/Multiply3'
                                        */
  real_T Multiply2_Gain;               /* Expression: 0.1
                                        * Referenced by: '<S2>/Multiply2'
                                        */
  real_T Constant_Value_j;             /* Expression: 5
                                        * Referenced by: '<S2>/Constant'
                                        */
  real_T Constant2_Value;              /* Expression: 100
                                        * Referenced by: '<S2>/Constant2'
                                        */
  real_T Multiply7_Gain;               /* Expression: 10
                                        * Referenced by: '<S2>/Multiply7'
                                        */
  real_T AtriumReferencePWM_Value;     /* Expression: 80
                                        * Referenced by: '<S2>/Atrium Reference PWM'
                                        */
  real_T Multiply4_Gain;               /* Expression: 0.01
                                        * Referenced by: '<S2>/Multiply4'
                                        */
  real_T Multiply1_Gain;               /* Expression: 0.1
                                        * Referenced by: '<S2>/Multiply1'
                                        */
  real_T Constant1_Value;              /* Expression: 5
                                        * Referenced by: '<S2>/Constant1'
                                        */
  real_T Constant3_Value;              /* Expression: 100
                                        * Referenced by: '<S2>/Constant3'
                                        */
  real_T Multiply8_Gain;               /* Expression: 10
                                        * Referenced by: '<S2>/Multiply8'
                                        */
  real_T VentricleReferencePWM_Value;  /* Expression: 80
                                        * Referenced by: '<S2>/Ventricle Reference PWM'
                                        */
  real_T Constant2_Value_b;            /* Expression: 1
                                        * Referenced by: '<S4>/Constant2'
                                        */
  real_T Accel_Smooth_Gain;            /* Expression: 20
                                        * Referenced by: '<S4>/Accel_Smooth'
                                        */
  real_T Multiply10_Gain;              /* Expression: 60
                                        * Referenced by: '<S2>/Multiply10'
                                        */
  real_T onoff_Value;                  /* Expression: 4
                                        * Referenced by: '<S2>/on//off'
                                        */
  real_T UnitDelay_InitialCondition;   /* Expression: 0
                                        * Referenced by: '<S4>/Unit Delay'
                                        */
  real32_T Gain_Gain;                  /* Computed Parameter: Gain_Gain
                                        * Referenced by: '<S2>/Gain'
                                        */
  real32_T Gain1_Gain;                 /* Computed Parameter: Gain1_Gain
                                        * Referenced by: '<S2>/Gain1'
                                        */
  uint8_T Constant1_Value_i;           /* Computed Parameter: Constant1_Value_i
                                        * Referenced by: '<S5>/Constant1'
                                        */
};

/* Real-time Model Data Structure */
struct tag_RTM_SerialMaster_T {
  const char_T * volatile errorStatus;
};

/* Block parameters (default storage) */
extern P_SerialMaster_T SerialMaster_P;

/* Block signals (default storage) */
extern B_SerialMaster_T SerialMaster_B;

/* Block states (default storage) */
extern DW_SerialMaster_T SerialMaster_DW;

/* Model entry point functions */
extern void SerialMaster_initialize(void);
extern void SerialMaster_step(void);
extern void SerialMaster_terminate(void);

/* Real-time Model object */
extern RT_MODEL_SerialMaster_T *const SerialMaster_M;
extern volatile boolean_T stopRequested;
extern volatile boolean_T runModel;

/*-
 * These blocks were eliminated from the model due to optimizations:
 *
 * Block '<S1>/OR' : Unused code path elimination
 * Block '<S2>/Cast To Double11' : Unused code path elimination
 * Block '<S2>/Cast To Double3' : Unused code path elimination
 * Block '<S2>/Cast To Double7' : Unused code path elimination
 * Block '<S2>/Cast To Double8' : Unused code path elimination
 * Block '<S2>/Multiply' : Unused code path elimination
 * Block '<S2>/Multiply5' : Unused code path elimination
 * Block '<S2>/Multiply6' : Unused code path elimination
 * Block '<S2>/Multiply9' : Unused code path elimination
 */

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'SerialMaster'
 * '<S1>'   : 'SerialMaster/HARDWARE OUTPUTS'
 * '<S2>'   : 'SerialMaster/INPUTS'
 * '<S3>'   : 'SerialMaster/PACEMAKER STATEFLOW'
 * '<S4>'   : 'SerialMaster/Rate Adaptive'
 * '<S5>'   : 'SerialMaster/INPUTS/COM_OUT '
 * '<S6>'   : 'SerialMaster/INPUTS/Chart2'
 * '<S7>'   : 'SerialMaster/Rate Adaptive/MATLAB Function'
 */
#endif                                 /* RTW_HEADER_SerialMaster_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
