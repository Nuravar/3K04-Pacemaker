/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: send_DCM.c
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

#include "SerialMaster_types.h"
#include "send_DCM_private.h"
#include "SerialMaster.h"
#include "send_DCM.h"
#include <string.h>
#include "rtwtypes.h"
#include <stddef.h>

/* Forward declaration for local functions */
static void SerialMaster_SystemCore_setup(freedomk64f_SCIWrite_SerialMa_T *obj);
static void SerialMaster_SystemCore_setup(freedomk64f_SCIWrite_SerialMa_T *obj)
{
  uint32_T SCIModuleLoc;

  /* Start for MATLABSystem: '<S5>/Serial Transmit1' */
  obj->isInitialized = 1;
  SCIModuleLoc = 0;

  /* Start for MATLABSystem: '<S5>/Serial Transmit1' */
  obj->MW_SCIHANDLE = MW_SCI_Open(&SCIModuleLoc, false, MW_UNDEFINED_VALUE, 10U);
  MW_SCI_SetBaudrate(obj->MW_SCIHANDLE, 115200U);
  MW_SCI_SetFrameFormat(obj->MW_SCIHANDLE, 8, MW_SCI_PARITY_NONE,
                        MW_SCI_STOPBITS_1);
  obj->isSetupComplete = true;
}

/* System initialize for Simulink Function: '<S2>/COM_OUT ' */
void send_DCM_Init(void)
{
  /* Start for MATLABSystem: '<S5>/Serial Transmit1' */
  SerialMaster_DW.obj_o.isInitialized = 0;
  SerialMaster_DW.obj_o.matlabCodegenIsDeleted = false;
  SerialMaster_SystemCore_setup(&SerialMaster_DW.obj_o);
}

/* Output and update for Simulink Function: '<S2>/COM_OUT ' */
void send_DCM(void)
{
  uint8_T TxDataLocChar[18];
  uint8_T rtb_Switch[18];
  uint8_T status;

  /* SignalConversion generated from: '<S5>/ATRSignal' */
  SerialMaster_B.TmpLatchAtATRSignalOutport1 = SerialMaster_B.Gain;

  /* SignalConversion generated from: '<S5>/VENTSignal' */
  SerialMaster_B.TmpLatchAtVENTSignalOutport1 = SerialMaster_B.Gain1;

  /* S-Function (any2byte): '<S5>/Byte Pack' */

  /* Pack: <S5>/Byte Pack */
  (void) memcpy(&SerialMaster_B.BytePack[0],
                &SerialMaster_B.TmpLatchAtATRSignalOutport1,
                4);

  /* S-Function (any2byte): '<S5>/Byte Pack1' */

  /* Pack: <S5>/Byte Pack1 */
  (void) memcpy(&SerialMaster_B.BytePack1[0],
                &SerialMaster_B.TmpLatchAtVENTSignalOutport1,
                4);

  /* Switch: '<S5>/Switch' incorporates:
   *  Constant: '<S5>/Constant'
   *  Constant: '<S5>/Constant1'
   *  SignalConversion generated from: '<S5>/AAmp'
   *  SignalConversion generated from: '<S5>/APulseWidth'
   *  SignalConversion generated from: '<S5>/ARP'
   *  SignalConversion generated from: '<S5>/ASensitivity'
   *  SignalConversion generated from: '<S5>/AVDelay'
   *  SignalConversion generated from: '<S5>/ActivityThreshold'
   *  SignalConversion generated from: '<S5>/LRL'
   *  SignalConversion generated from: '<S5>/MSR'
   *  SignalConversion generated from: '<S5>/Mode'
   *  SignalConversion generated from: '<S5>/PVARP'
   *  SignalConversion generated from: '<S5>/ReactionTime'
   *  SignalConversion generated from: '<S5>/RecoveryTime'
   *  SignalConversion generated from: '<S5>/ResponseFactor'
   *  SignalConversion generated from: '<S5>/URL'
   *  SignalConversion generated from: '<S5>/VAmp'
   *  SignalConversion generated from: '<S5>/VPulseWidth'
   *  SignalConversion generated from: '<S5>/VRP'
   *  SignalConversion generated from: '<S5>/VSensitivity'
   */
  if (SerialMaster_P.Constant_Value != 0.0) {
    rtb_Switch[0] = SerialMaster_B.Mode;
    rtb_Switch[1] = SerialMaster_B.LRL;
    rtb_Switch[2] = SerialMaster_B.URL;
    rtb_Switch[3] = SerialMaster_B.MSR;
    rtb_Switch[4] = SerialMaster_B.AVDelay;
    rtb_Switch[5] = SerialMaster_B.AAmp;
    rtb_Switch[6] = SerialMaster_B.VAmp;
    rtb_Switch[7] = SerialMaster_B.APulseWidth;
    rtb_Switch[8] = SerialMaster_B.VPulseWidth;
    rtb_Switch[9] = SerialMaster_B.ASensitivity;
    rtb_Switch[10] = SerialMaster_B.VSensitivity;
    rtb_Switch[11] = SerialMaster_B.ARP;
    rtb_Switch[12] = SerialMaster_B.VRP;
    rtb_Switch[13] = SerialMaster_B.PVARP;
    rtb_Switch[14] = SerialMaster_B.ActivityThreshold;
    rtb_Switch[15] = SerialMaster_B.ReactionTime;
    rtb_Switch[16] = SerialMaster_B.ResponseFactor;
    rtb_Switch[17] = SerialMaster_B.RecoveryTime;
  } else {
    rtb_Switch[0] = SerialMaster_B.BytePack[0];
    rtb_Switch[1] = SerialMaster_B.BytePack[1];
    rtb_Switch[2] = SerialMaster_B.BytePack[2];
    rtb_Switch[3] = SerialMaster_B.BytePack[3];
    rtb_Switch[4] = SerialMaster_B.BytePack1[0];
    rtb_Switch[5] = SerialMaster_B.BytePack1[1];
    rtb_Switch[6] = SerialMaster_B.BytePack1[2];
    rtb_Switch[7] = SerialMaster_B.BytePack1[3];
    rtb_Switch[8] = SerialMaster_P.Constant1_Value_i;
    rtb_Switch[9] = SerialMaster_P.Constant1_Value_i;
    rtb_Switch[10] = SerialMaster_P.Constant1_Value_i;
    rtb_Switch[11] = SerialMaster_P.Constant1_Value_i;
    rtb_Switch[12] = SerialMaster_P.Constant1_Value_i;
    rtb_Switch[13] = SerialMaster_P.Constant1_Value_i;
    rtb_Switch[14] = SerialMaster_P.Constant1_Value_i;
    rtb_Switch[15] = SerialMaster_P.Constant1_Value_i;
    rtb_Switch[16] = SerialMaster_P.Constant1_Value_i;
    rtb_Switch[17] = SerialMaster_P.Constant1_Value_i;
  }

  /* End of Switch: '<S5>/Switch' */

  /* MATLABSystem: '<S5>/Serial Transmit1' */
  status = 1U;
  while (status != 0) {
    memcpy((void *)&TxDataLocChar[0], (void *)&rtb_Switch[0], (size_t)18 *
           sizeof(uint8_T));
    status = MW_SCI_Transmit(SerialMaster_DW.obj_o.MW_SCIHANDLE, &TxDataLocChar
      [0], 18U);
  }

  /* End of MATLABSystem: '<S5>/Serial Transmit1' */
}

/* Termination for Simulink Function: '<S2>/COM_OUT ' */
void send_DCM_Term(void)
{
  /* Terminate for MATLABSystem: '<S5>/Serial Transmit1' */
  if (!SerialMaster_DW.obj_o.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_o.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_o.isInitialized == 1) &&
        SerialMaster_DW.obj_o.isSetupComplete) {
      MW_SCI_Close(SerialMaster_DW.obj_o.MW_SCIHANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S5>/Serial Transmit1' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
