/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: send_DCM_private.h
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

#ifndef RTW_HEADER_send_DCM_private_h_
#define RTW_HEADER_send_DCM_private_h_
#ifndef SerialMaster_COMMON_INCLUDES_
#define SerialMaster_COMMON_INCLUDES_
#include "rtwtypes.h"
#include "MW_digitalIO.h"
#include "MW_PWM.h"
#include "MW_AnalogIn.h"
#include "MW_SCI.h"
#include "MW_I2C.h"
#endif                                 /* SerialMaster_COMMON_INCLUDES_ */

extern void send_DCM_Init(void);
extern void send_DCM_Term(void);

#endif                                 /* RTW_HEADER_send_DCM_private_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
