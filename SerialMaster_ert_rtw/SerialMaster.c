/*
 * Academic License - for use in teaching, academic research, and meeting
 * course requirements at degree granting institutions only.  Not for
 * government, commercial, or other organizational use.
 *
 * File: SerialMaster.c
 *
 * Code generated for Simulink model 'SerialMaster'.
 *
 * Model version                  : 1.29
 * Simulink Coder version         : 23.2 (R2023b) 01-Aug-2023
 * C/C++ source code generated on : Sun Nov 26 03:53:18 2023
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "SerialMaster.h"
#include "SerialMaster_types.h"
#include "rtwtypes.h"
#include <string.h>
#include <math.h>
#include <stddef.h>
#include "send_DCM.h"
#include "send_DCM_private.h"

/* Named constants for Chart: '<S2>/Chart2' */
#define SerialMaster_IN_Default        ((uint8_T)1U)
#define SerialMaster_IN_NO_ACTIVE_CHILD ((uint8_T)0U)
#define SerialMaster_IN_ReturnData     ((uint8_T)2U)
#define SerialMaster_IN_Send_EGRAM     ((uint8_T)3U)
#define SerialMaster_IN_Send_EGRAM2    ((uint8_T)4U)
#define SerialMaster_IN_WaitBuffer     ((uint8_T)5U)
#define SerialMaster_IN_entry_         ((uint8_T)6U)
#define SerialMaster_IN_entry_1        ((uint8_T)7U)
#define SerialMaster_IN_hehe           ((uint8_T)8U)
#define SerialMaster_IN_name           ((uint8_T)9U)

/* Named constants for Chart: '<Root>/PACEMAKER STATEFLOW' */
#define SerialMaster_IN_AAI            ((uint8_T)1U)
#define SerialMaster_IN_AOO            ((uint8_T)2U)
#define SerialMaster_IN_Pace           ((uint8_T)1U)
#define SerialMaster_IN_Refractory     ((uint8_T)2U)
#define SerialMaster_IN_Sense          ((uint8_T)3U)
#define SerialMaster_IN_VOO            ((uint8_T)3U)
#define SerialMaster_IN_VVI            ((uint8_T)4U)
#define SerialMaster_IN_waiting        ((uint8_T)4U)

/* Block signals (default storage) */
B_SerialMaster_T SerialMaster_B;

/* Block states (default storage) */
DW_SerialMaster_T SerialMaster_DW;

/* Real-time model */
static RT_MODEL_SerialMaster_T SerialMaster_M_;
RT_MODEL_SerialMaster_T *const SerialMaster_M = &SerialMaster_M_;

/* Forward declaration for local functions */
static void Ser_enter_atomic_Refractory_f3x(const real_T *Product1, const real_T
  *Target_Rate);
static void Seria_enter_atomic_Refractory_f(const real_T *Product, const real_T *
  Target_Rate);
static void SerialM_enter_atomic_Refractory(const real_T *Product, const real_T *
  Target_Rate);
static void Seri_enter_atomic_Refractory_f3(const real_T *Product1, const real_T
  *Target_Rate);
static void SerialMaster_VVI(const real_T *Product, const real_T *Multiply4,
  const real_T *Multiply8, const real_T *Product1, const real_T *Target_Rate,
  const boolean_T *DigitalRead1);
static void SerialMaster_AAI(const real_T *Multiply3, const real_T *Product,
  const real_T *Multiply7, const real_T *Product1, const real_T *Target_Rate,
  const boolean_T *DigitalRead);
static void SerialMaster_SystemCore_setup_d(freedomk64f_SCIRead_SerialMas_T *obj);
static void SerialMast_SystemCore_setup_drh(freedomk64f_fxos8700_SerialMa_T *obj);
static void SerialMaste_SystemCore_setup_dr(dsp_simulink_MovingAverage_Se_T *obj);

/* Function for Chart: '<Root>/PACEMAKER STATEFLOW' */
static void Ser_enter_atomic_Refractory_f3x(const real_T *Product1, const real_T
  *Target_Rate)
{
  SerialMaster_B.D5_PACING_REF_PWM = *Product1;
  SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
  SerialMaster_B.D9_VENT_PACE_CTRL = 0.0;
  SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
  SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
  SerialMaster_B.D8_ATR_PACE_CTRL = 0.0;
  SerialMaster_B.D11_ATR_GND_CTRL = 0.0;
  SerialMaster_B.D12_VENT_GND_CTRL = 1.0;
  SerialMaster_B.D2_PACE_CHARGE_CTRL = 1.0;

  /* Constant: '<S2>/Ventricle Reference PWM' */
  SerialMaster_B.D3_VENT_CMP_REF_PWM =
    SerialMaster_P.VentricleReferencePWM_Value;
  SerialMaster_DW.Standby_Period = 30000.0 / *Target_Rate;
}

/* Function for Chart: '<Root>/PACEMAKER STATEFLOW' */
static void Seria_enter_atomic_Refractory_f(const real_T *Product, const real_T *
  Target_Rate)
{
  SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
  SerialMaster_B.D9_VENT_PACE_CTRL = 0.0;
  SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
  SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
  SerialMaster_B.D8_ATR_PACE_CTRL = 0.0;
  SerialMaster_B.D11_ATR_GND_CTRL = 1.0;
  SerialMaster_B.D12_VENT_GND_CTRL = 0.0;
  SerialMaster_B.D2_PACE_CHARGE_CTRL = 1.0;
  SerialMaster_B.D5_PACING_REF_PWM = *Product;
  SerialMaster_DW.Standby_Period = 1.0 / *Target_Rate * 30000.0;
}

/* Function for Chart: '<Root>/PACEMAKER STATEFLOW' */
static void SerialM_enter_atomic_Refractory(const real_T *Product, const real_T *
  Target_Rate)
{
  SerialMaster_B.D5_PACING_REF_PWM = *Product;
  SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
  SerialMaster_B.D9_VENT_PACE_CTRL = 0.0;
  SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
  SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
  SerialMaster_B.D8_ATR_PACE_CTRL = 0.0;
  SerialMaster_B.D11_ATR_GND_CTRL = 1.0;
  SerialMaster_B.D12_VENT_GND_CTRL = 0.0;
  SerialMaster_B.D2_PACE_CHARGE_CTRL = 1.0;

  /* Constant: '<S2>/Atrium Reference PWM' */
  SerialMaster_B.D6_ATR_CMP_REF_PWM = SerialMaster_P.AtriumReferencePWM_Value;
  SerialMaster_DW.Standby_Period = 30000.0 / *Target_Rate;
}

/* Function for Chart: '<Root>/PACEMAKER STATEFLOW' */
static void Seri_enter_atomic_Refractory_f3(const real_T *Product1, const real_T
  *Target_Rate)
{
  SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
  SerialMaster_B.D9_VENT_PACE_CTRL = 0.0;
  SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
  SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
  SerialMaster_B.D8_ATR_PACE_CTRL = 0.0;
  SerialMaster_B.D11_ATR_GND_CTRL = 0.0;
  SerialMaster_B.D12_VENT_GND_CTRL = 1.0;
  SerialMaster_B.D2_PACE_CHARGE_CTRL = 1.0;
  SerialMaster_B.D5_PACING_REF_PWM = *Product1;
  SerialMaster_DW.Standby_Period = 1.0 / *Target_Rate * 30000.0;
}

/* Function for Chart: '<Root>/PACEMAKER STATEFLOW' */
static void SerialMaster_VVI(const real_T *Product, const real_T *Multiply4,
  const real_T *Multiply8, const real_T *Product1, const real_T *Target_Rate,
  const boolean_T *DigitalRead1)
{
  if ((SerialMaster_B.Mode == 1) || (SerialMaster_B.Mode == 5)) {
    SerialMaster_DW.is_VVI = SerialMaster_IN_NO_ACTIVE_CHILD;
    SerialMaster_DW.is_c3_SerialMaster = SerialMaster_IN_VOO;
    SerialMaster_DW.temporalCounter_i1 = 0U;
    SerialMaster_DW.is_VOO = SerialMaster_IN_Refractory;
    Seri_enter_atomic_Refractory_f3(Product1, Target_Rate);
  } else if ((SerialMaster_B.Mode == 2) || (SerialMaster_B.Mode == 6)) {
    SerialMaster_DW.is_VVI = SerialMaster_IN_NO_ACTIVE_CHILD;
    SerialMaster_DW.is_c3_SerialMaster = SerialMaster_IN_AAI;
    SerialMaster_DW.is_AAI = SerialMaster_IN_Refractory;
    SerialM_enter_atomic_Refractory(Product, Target_Rate);
  } else if ((SerialMaster_B.Mode == 0) || (SerialMaster_B.Mode == 4)) {
    SerialMaster_DW.is_VVI = SerialMaster_IN_NO_ACTIVE_CHILD;
    SerialMaster_DW.is_c3_SerialMaster = SerialMaster_IN_AOO;
    SerialMaster_DW.temporalCounter_i1 = 0U;
    SerialMaster_DW.is_AOO = SerialMaster_IN_Refractory;
    Seria_enter_atomic_Refractory_f(Product, Target_Rate);
  } else {
    switch (SerialMaster_DW.is_VVI) {
     case SerialMaster_IN_Pace:
      SerialMaster_B.D2_PACE_CHARGE_CTRL = 0.0;
      SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
      SerialMaster_B.D8_ATR_PACE_CTRL = 0.0;
      SerialMaster_B.D11_ATR_GND_CTRL = 0.0;
      SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
      SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
      SerialMaster_B.D12_VENT_GND_CTRL = 0.0;
      SerialMaster_B.D9_VENT_PACE_CTRL = 1.0;
      if (SerialMaster_DW.temporalCounter_i1 >= (uint32_T)ceil(*Multiply4)) {
        SerialMaster_DW.is_VVI = SerialMaster_IN_Refractory;
        Ser_enter_atomic_Refractory_f3x(Product1, Target_Rate);
      }
      break;

     case SerialMaster_IN_Refractory:
      SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
      SerialMaster_B.D9_VENT_PACE_CTRL = 0.0;
      SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
      SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
      SerialMaster_B.D8_ATR_PACE_CTRL = 0.0;
      SerialMaster_B.D11_ATR_GND_CTRL = 0.0;
      SerialMaster_B.D12_VENT_GND_CTRL = 1.0;
      SerialMaster_B.D2_PACE_CHARGE_CTRL = 1.0;
      SerialMaster_DW.temporalCounter_i1 = 0U;
      SerialMaster_DW.is_VVI = SerialMaster_IN_waiting;
      break;

     case SerialMaster_IN_Sense:
      if (SerialMaster_DW.temporalCounter_i1 >= (uint32_T)ceil
          ((SerialMaster_DW.Standby_Period - *Multiply4) - *Multiply8)) {
        SerialMaster_DW.temporalCounter_i1 = 0U;
        SerialMaster_DW.is_VVI = SerialMaster_IN_Pace;
        SerialMaster_B.D5_PACING_REF_PWM = 0.0;
        SerialMaster_B.D2_PACE_CHARGE_CTRL = 0.0;
        SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
        SerialMaster_B.D8_ATR_PACE_CTRL = 0.0;
        SerialMaster_B.D11_ATR_GND_CTRL = 0.0;
        SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
        SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
        SerialMaster_B.D12_VENT_GND_CTRL = 0.0;
        SerialMaster_B.D9_VENT_PACE_CTRL = 1.0;
      } else if (*DigitalRead1) {
        SerialMaster_DW.temporalCounter_i1 = 0U;
        SerialMaster_DW.is_VVI = SerialMaster_IN_waiting;
      }
      break;

     default:
      /* case IN_waiting: */
      if (SerialMaster_DW.temporalCounter_i1 >= (uint32_T)ceil(*Multiply8)) {
        SerialMaster_DW.temporalCounter_i1 = 0U;
        SerialMaster_DW.is_VVI = SerialMaster_IN_Sense;
      }
      break;
    }
  }
}

/* Function for Chart: '<Root>/PACEMAKER STATEFLOW' */
static void SerialMaster_AAI(const real_T *Multiply3, const real_T *Product,
  const real_T *Multiply7, const real_T *Product1, const real_T *Target_Rate,
  const boolean_T *DigitalRead)
{
  if ((SerialMaster_B.Mode == 3) || (SerialMaster_B.Mode == 7)) {
    SerialMaster_DW.is_AAI = SerialMaster_IN_NO_ACTIVE_CHILD;
    SerialMaster_DW.is_c3_SerialMaster = SerialMaster_IN_VVI;
    SerialMaster_DW.is_VVI = SerialMaster_IN_Refractory;
    Ser_enter_atomic_Refractory_f3x(Product1, Target_Rate);
  } else if ((SerialMaster_B.Mode == 0) || (SerialMaster_B.Mode == 4)) {
    SerialMaster_DW.is_AAI = SerialMaster_IN_NO_ACTIVE_CHILD;
    SerialMaster_DW.is_c3_SerialMaster = SerialMaster_IN_AOO;
    SerialMaster_DW.temporalCounter_i1 = 0U;
    SerialMaster_DW.is_AOO = SerialMaster_IN_Refractory;
    Seria_enter_atomic_Refractory_f(Product, Target_Rate);
  } else if ((SerialMaster_B.Mode == 1) || (SerialMaster_B.Mode == 5)) {
    SerialMaster_DW.is_AAI = SerialMaster_IN_NO_ACTIVE_CHILD;
    SerialMaster_DW.is_c3_SerialMaster = SerialMaster_IN_VOO;
    SerialMaster_DW.temporalCounter_i1 = 0U;
    SerialMaster_DW.is_VOO = SerialMaster_IN_Refractory;
    Seri_enter_atomic_Refractory_f3(Product1, Target_Rate);
  } else {
    switch (SerialMaster_DW.is_AAI) {
     case SerialMaster_IN_Pace:
      SerialMaster_B.D2_PACE_CHARGE_CTRL = 0.0;
      SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
      SerialMaster_B.D8_ATR_PACE_CTRL = 1.0;
      SerialMaster_B.D11_ATR_GND_CTRL = 0.0;
      SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
      SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
      SerialMaster_B.D12_VENT_GND_CTRL = 0.0;
      SerialMaster_B.D9_VENT_PACE_CTRL = 0.0;
      if (SerialMaster_DW.temporalCounter_i1 >= (uint32_T)ceil(*Multiply3)) {
        SerialMaster_DW.is_AAI = SerialMaster_IN_Refractory;
        SerialM_enter_atomic_Refractory(Product, Target_Rate);
      }
      break;

     case SerialMaster_IN_Refractory:
      SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
      SerialMaster_B.D9_VENT_PACE_CTRL = 0.0;
      SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
      SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
      SerialMaster_B.D8_ATR_PACE_CTRL = 0.0;
      SerialMaster_B.D11_ATR_GND_CTRL = 1.0;
      SerialMaster_B.D12_VENT_GND_CTRL = 0.0;
      SerialMaster_B.D2_PACE_CHARGE_CTRL = 1.0;
      SerialMaster_DW.temporalCounter_i1 = 0U;
      SerialMaster_DW.is_AAI = SerialMaster_IN_waiting;
      break;

     case SerialMaster_IN_Sense:
      if (SerialMaster_DW.temporalCounter_i1 >= (uint32_T)ceil
          ((SerialMaster_DW.Standby_Period - *Multiply3) - *Multiply7)) {
        SerialMaster_DW.temporalCounter_i1 = 0U;
        SerialMaster_DW.is_AAI = SerialMaster_IN_Pace;
        SerialMaster_B.D5_PACING_REF_PWM = 0.0;
        SerialMaster_B.D2_PACE_CHARGE_CTRL = 0.0;
        SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
        SerialMaster_B.D8_ATR_PACE_CTRL = 1.0;
        SerialMaster_B.D11_ATR_GND_CTRL = 0.0;
        SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
        SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
        SerialMaster_B.D12_VENT_GND_CTRL = 0.0;
        SerialMaster_B.D9_VENT_PACE_CTRL = 0.0;
      } else if (*DigitalRead) {
        SerialMaster_DW.temporalCounter_i1 = 0U;
        SerialMaster_DW.is_AAI = SerialMaster_IN_waiting;
      }
      break;

     default:
      /* case IN_waiting: */
      if (SerialMaster_DW.temporalCounter_i1 >= (uint32_T)ceil(*Multiply7)) {
        SerialMaster_DW.temporalCounter_i1 = 0U;
        SerialMaster_DW.is_AAI = SerialMaster_IN_Sense;
      }
      break;
    }
  }
}

static void SerialMaster_SystemCore_setup_d(freedomk64f_SCIRead_SerialMas_T *obj)
{
  uint32_T SCIModuleLoc;

  /* Start for MATLABSystem: '<S2>/Serial Receive1' */
  obj->isInitialized = 1;
  SCIModuleLoc = 0;

  /* Start for MATLABSystem: '<S2>/Serial Receive1' */
  obj->MW_SCIHANDLE = MW_SCI_Open(&SCIModuleLoc, false, 10U, MW_UNDEFINED_VALUE);
  MW_SCI_SetBaudrate(obj->MW_SCIHANDLE, 115200U);
  MW_SCI_SetFrameFormat(obj->MW_SCIHANDLE, 8, MW_SCI_PARITY_NONE,
                        MW_SCI_STOPBITS_1);
  obj->isSetupComplete = true;
}

static void SerialMast_SystemCore_setup_drh(freedomk64f_fxos8700_SerialMa_T *obj)
{
  uint8_T b_SwappedDataBytes[2];
  uint8_T b_RegisterValue;
  uint8_T status;

  /* Start for MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor1' */
  obj->isInitialized = 1;
  obj->i2cobj.MW_I2C_HANDLE = MW_I2C_Open(0, MW_I2C_MASTER);
  obj->i2cobj.BusSpeed = 100000U;
  MW_I2C_SetBusSpeed(obj->i2cobj.MW_I2C_HANDLE, obj->i2cobj.BusSpeed);
  b_SwappedDataBytes[0] = 43U;
  b_SwappedDataBytes[1] = 64U;
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U, &b_SwappedDataBytes[0], 2U,
                     false, false);
  OSA_TimeDelay(500U);
  status = 42U;

  /* Start for MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor1' */
  status = MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U, &status, 1U, true,
    false);
  if (status == 0) {
    MW_I2C_MasterRead(obj->i2cobj.MW_I2C_HANDLE, 29U, &status, 1U, false, true);
    memcpy((void *)&b_RegisterValue, (void *)&status, (size_t)1 * sizeof(uint8_T));
  } else {
    b_RegisterValue = 0U;
  }

  b_SwappedDataBytes[0] = 42U;

  /* Start for MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor1' */
  b_SwappedDataBytes[1] = (uint8_T)(b_RegisterValue & 254);
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U, &b_SwappedDataBytes[0], 2U,
                     false, false);
  b_SwappedDataBytes[0] = 14U;
  b_SwappedDataBytes[1] = 1U;
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U, &b_SwappedDataBytes[0], 2U,
                     false, false);
  b_SwappedDataBytes[0] = 91U;
  b_SwappedDataBytes[1] = 0U;
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U, &b_SwappedDataBytes[0], 2U,
                     false, false);
  b_SwappedDataBytes[0] = 42U;
  b_SwappedDataBytes[1] = 1U;
  MW_I2C_MasterWrite(obj->i2cobj.MW_I2C_HANDLE, 29U, &b_SwappedDataBytes[0], 2U,
                     false, false);
  obj->isSetupComplete = true;
}

static void SerialMaste_SystemCore_setup_dr(dsp_simulink_MovingAverage_Se_T *obj)
{
  obj->isSetupComplete = false;
  obj->isInitialized = 1;

  /* Start for MATLABSystem: '<S4>/ ' */
  obj->NumChannels = 1;
  obj->FrameLength = 1;
  obj->_pobj0.isInitialized = 0;
  obj->_pobj0.isInitialized = 0;
  obj->pStatistic = &obj->_pobj0;
  obj->isSetupComplete = true;
  obj->TunablePropsChanged = false;
}

/* Model step function */
void SerialMaster_step(void)
{
  h_dsp_internal_SlidingWindowA_T *obj;
  int32_T i;
  uint8_T output_raw[6];
  uint8_T b_x[2];
  uint8_T y[2];
  uint8_T status;
  boolean_T DigitalRead;
  boolean_T DigitalRead1;
  boolean_T rtb_DigitalRead4_0;

  /* MATLABSystem: '<S2>/Digital Read' */
  if (SerialMaster_DW.obj_c.SampleTime != SerialMaster_P.DigitalRead_SampleTime)
  {
    SerialMaster_DW.obj_c.SampleTime = SerialMaster_P.DigitalRead_SampleTime;
  }

  /* MATLABSystem: '<S2>/Digital Read' */
  DigitalRead = MW_digitalIO_read(SerialMaster_DW.obj_c.MW_DIGITALIO_HANDLE);

  /* MATLABSystem: '<S2>/Digital Read1' */
  if (SerialMaster_DW.obj_bt.SampleTime !=
      SerialMaster_P.DigitalRead1_SampleTime) {
    SerialMaster_DW.obj_bt.SampleTime = SerialMaster_P.DigitalRead1_SampleTime;
  }

  /* MATLABSystem: '<S2>/Digital Read1' */
  DigitalRead1 = MW_digitalIO_read(SerialMaster_DW.obj_bt.MW_DIGITALIO_HANDLE);

  /* MATLABSystem: '<S2>/Serial Receive1' */
  if (SerialMaster_DW.obj_k3.SampleTime !=
      SerialMaster_P.SerialReceive1_SampleTime) {
    SerialMaster_DW.obj_k3.SampleTime = SerialMaster_P.SerialReceive1_SampleTime;
  }

  status = MW_SCI_Receive(SerialMaster_DW.obj_k3.MW_SCIHANDLE,
    &SerialMaster_B.RxDataLocChar[0], 20U);
  memcpy((void *)&SerialMaster_B.RxData[0], (void *)
         &SerialMaster_B.RxDataLocChar[0], (size_t)20 * sizeof(uint8_T));

  /* MATLABSystem: '<S2>/Digital Read4' */
  if (SerialMaster_DW.obj_h.SampleTime != SerialMaster_P.DigitalRead4_SampleTime)
  {
    SerialMaster_DW.obj_h.SampleTime = SerialMaster_P.DigitalRead4_SampleTime;
  }

  rtb_DigitalRead4_0 = MW_digitalIO_read
    (SerialMaster_DW.obj_h.MW_DIGITALIO_HANDLE);

  /* Gain: '<S2>/Gain' incorporates:
   *  DataTypeConversion: '<S2>/Data Type Conversion3'
   *  MATLABSystem: '<S2>/Digital Read4'
   */
  SerialMaster_B.Gain = SerialMaster_P.Gain_Gain * (real32_T)rtb_DigitalRead4_0;

  /* MATLABSystem: '<S2>/Digital Read5' */
  if (SerialMaster_DW.obj_b.SampleTime != SerialMaster_P.DigitalRead5_SampleTime)
  {
    SerialMaster_DW.obj_b.SampleTime = SerialMaster_P.DigitalRead5_SampleTime;
  }

  rtb_DigitalRead4_0 = MW_digitalIO_read
    (SerialMaster_DW.obj_b.MW_DIGITALIO_HANDLE);

  /* Gain: '<S2>/Gain1' incorporates:
   *  DataTypeConversion: '<S2>/Data Type Conversion2'
   *  MATLABSystem: '<S2>/Digital Read5'
   */
  SerialMaster_B.Gain1 = SerialMaster_P.Gain1_Gain * (real32_T)
    rtb_DigitalRead4_0;

  /* Chart: '<S2>/Chart2' incorporates:
   *  MATLABSystem: '<S2>/Serial Receive1'
   * */
  if (SerialMaster_DW.temporalCounter_i1_f < 31U) {
    SerialMaster_DW.temporalCounter_i1_f++;
  }

  if (SerialMaster_DW.is_active_c4_SerialMaster == 0U) {
    SerialMaster_DW.is_active_c4_SerialMaster = 1U;
    SerialMaster_DW.is_c4_SerialMaster = SerialMaster_IN_Default;
    SerialMaster_B.Mode = 1U;
    SerialMaster_B.LRL = 60U;
    SerialMaster_B.URL = 120U;
    SerialMaster_B.MSR = 120U;
    SerialMaster_B.AVDelay = 150U;
    SerialMaster_B.AAmp = 35U;
    SerialMaster_B.VAmp = 35U;
    SerialMaster_B.APulseWidth = 40U;
    SerialMaster_B.VPulseWidth = 40U;
    SerialMaster_B.ASensitivity = 15U;
    SerialMaster_B.VSensitivity = 50U;
    SerialMaster_B.ARP = 25U;
    SerialMaster_B.VRP = 32U;
    SerialMaster_B.PVARP = 32U;
    SerialMaster_B.ActivityThreshold = 4U;
    SerialMaster_B.ReactionTime = 30U;
    SerialMaster_B.ResponseFactor = 8U;
    SerialMaster_B.RecoveryTime = 5U;
    SerialMaster_B.GreenLED = false;
  } else {
    switch (SerialMaster_DW.is_c4_SerialMaster) {
     case SerialMaster_IN_Default:
      SerialMaster_DW.is_c4_SerialMaster = SerialMaster_IN_entry_1;
      break;

     case SerialMaster_IN_ReturnData:
      SerialMaster_DW.is_c4_SerialMaster = SerialMaster_IN_entry_1;
      break;

     case SerialMaster_IN_Send_EGRAM:
      SerialMaster_DW.is_c4_SerialMaster = SerialMaster_IN_Send_EGRAM2;
      send_DCM();
      SerialMaster_B.GreenLED = true;
      break;

     case SerialMaster_IN_Send_EGRAM2:
      SerialMaster_B.GreenLED = false;
      SerialMaster_DW.is_c4_SerialMaster = SerialMaster_IN_entry_1;
      break;

     case SerialMaster_IN_WaitBuffer:
      if (SerialMaster_DW.temporalCounter_i1_f >= 20U) {
        SerialMaster_DW.is_c4_SerialMaster = SerialMaster_IN_ReturnData;
        send_DCM();
      }
      break;

     case SerialMaster_IN_entry_:
      SerialMaster_DW.is_c4_SerialMaster = SerialMaster_IN_entry_1;
      break;

     case SerialMaster_IN_entry_1:
      if (status == 0) {
        SerialMaster_DW.SYNC = SerialMaster_B.RxData[0];
        SerialMaster_DW.FUNC = SerialMaster_B.RxData[1];
        SerialMaster_DW.MODEIN = SerialMaster_B.RxData[2];
        SerialMaster_DW.LRLIN = SerialMaster_B.RxData[3];
        SerialMaster_DW.URLIN = SerialMaster_B.RxData[4];
        SerialMaster_DW.MSRIN = SerialMaster_B.RxData[5];
        SerialMaster_DW.AVDelayIN = SerialMaster_B.RxData[6];
        SerialMaster_DW.AAmpIN = SerialMaster_B.RxData[7];
        SerialMaster_DW.VAmpIN = SerialMaster_B.RxData[8];
        SerialMaster_DW.APulseWidthIN = SerialMaster_B.RxData[9];
        SerialMaster_DW.VPulseWidthIN = SerialMaster_B.RxData[10];
        SerialMaster_DW.ASensitivityIN = SerialMaster_B.RxData[11];
        SerialMaster_DW.VSensitivityIN = SerialMaster_B.RxData[12];
        SerialMaster_DW.ARPIN = SerialMaster_B.RxData[13];
        SerialMaster_DW.VRPIN = SerialMaster_B.RxData[14];
        SerialMaster_DW.PVARPIN = SerialMaster_B.RxData[15];
        SerialMaster_DW.ActivityThresholdIN = SerialMaster_B.RxData[16];
        SerialMaster_DW.ReactionTimeIN = SerialMaster_B.RxData[17];
        SerialMaster_DW.ResponseFactorIN = SerialMaster_B.RxData[18];
        SerialMaster_DW.RecoveryTimeIN = SerialMaster_B.RxData[19];
        SerialMaster_DW.is_c4_SerialMaster = SerialMaster_IN_name;
      }
      break;

     case SerialMaster_IN_hehe:
      switch (SerialMaster_DW.FUNC) {
       case 85:
        SerialMaster_DW.is_c4_SerialMaster = SerialMaster_IN_entry_;
        SerialMaster_B.Mode = SerialMaster_DW.MODEIN;
        SerialMaster_B.LRL = SerialMaster_DW.LRLIN;
        SerialMaster_B.URL = SerialMaster_DW.URLIN;
        SerialMaster_B.MSR = SerialMaster_DW.MSRIN;
        SerialMaster_B.AVDelay = SerialMaster_DW.AVDelayIN;
        SerialMaster_B.AAmp = SerialMaster_DW.AAmpIN;
        SerialMaster_B.VAmp = SerialMaster_DW.VAmpIN;
        SerialMaster_B.APulseWidth = SerialMaster_DW.APulseWidthIN;
        SerialMaster_B.VPulseWidth = SerialMaster_DW.VPulseWidthIN;
        SerialMaster_B.ASensitivity = SerialMaster_DW.ASensitivityIN;
        SerialMaster_B.VSensitivity = SerialMaster_DW.VSensitivityIN;
        SerialMaster_B.ARP = SerialMaster_DW.ARPIN;
        SerialMaster_B.VRP = SerialMaster_DW.VRPIN;
        SerialMaster_B.PVARP = SerialMaster_DW.PVARPIN;
        SerialMaster_B.ActivityThreshold = SerialMaster_DW.ActivityThresholdIN;
        SerialMaster_B.ReactionTime = SerialMaster_DW.ReactionTimeIN;
        SerialMaster_B.ResponseFactor = SerialMaster_DW.ResponseFactorIN;
        SerialMaster_B.RecoveryTime = SerialMaster_DW.RecoveryTimeIN;
        break;

       case 34:
        SerialMaster_DW.temporalCounter_i1_f = 0U;
        SerialMaster_DW.is_c4_SerialMaster = SerialMaster_IN_WaitBuffer;
        break;

       case 56:
        SerialMaster_DW.is_c4_SerialMaster = SerialMaster_IN_Send_EGRAM;
        break;
      }
      break;

     default:
      /* case IN_name: */
      if (SerialMaster_DW.SYNC == 22) {
        SerialMaster_DW.is_c4_SerialMaster = SerialMaster_IN_hehe;
        SerialMaster_B.GreenLED = true;
      }
      break;
    }
  }

  /* End of Chart: '<S2>/Chart2' */

  /* Gain: '<S2>/Multiply3' incorporates:
   *  DataTypeConversion: '<S2>/Cast To Double5'
   */
  SerialMaster_B.Multiply3 = SerialMaster_P.Multiply3_Gain * (real_T)
    SerialMaster_B.APulseWidth;

  /* Product: '<S2>/Product' incorporates:
   *  Constant: '<S2>/Constant'
   *  Constant: '<S2>/Constant2'
   *  DataTypeConversion: '<S2>/Cast To Double16'
   *  Gain: '<S2>/Multiply2'
   *  Product: '<S2>/Divide'
   */
  SerialMaster_B.Product = SerialMaster_P.Multiply2_Gain * (real_T)
    SerialMaster_B.AAmp / SerialMaster_P.Constant_Value_j *
    SerialMaster_P.Constant2_Value;

  /* Gain: '<S2>/Multiply7' incorporates:
   *  DataTypeConversion: '<S2>/Cast To Double9'
   */
  SerialMaster_B.Multiply7 = SerialMaster_P.Multiply7_Gain * (real_T)
    SerialMaster_B.ARP;

  /* Gain: '<S2>/Multiply4' incorporates:
   *  DataTypeConversion: '<S2>/Cast To Double6'
   */
  SerialMaster_B.Multiply4 = SerialMaster_P.Multiply4_Gain * (real_T)
    SerialMaster_B.VPulseWidth;

  /* Product: '<S2>/Product1' incorporates:
   *  Constant: '<S2>/Constant1'
   *  Constant: '<S2>/Constant3'
   *  DataTypeConversion: '<S2>/Cast To Double4'
   *  Gain: '<S2>/Multiply1'
   *  Product: '<S2>/Divide1'
   */
  SerialMaster_B.Product1 = SerialMaster_P.Multiply1_Gain * (real_T)
    SerialMaster_B.VAmp / SerialMaster_P.Constant1_Value *
    SerialMaster_P.Constant3_Value;

  /* Gain: '<S2>/Multiply8' incorporates:
   *  DataTypeConversion: '<S2>/Cast To Double10'
   */
  SerialMaster_B.Multiply8 = SerialMaster_P.Multiply8_Gain * (real_T)
    SerialMaster_B.VRP;

  /* MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor1' */
  if (SerialMaster_DW.obj_k.SampleTime !=
      SerialMaster_P.FXOS87006AxesSensor1_SampleTime) {
    SerialMaster_DW.obj_k.SampleTime =
      SerialMaster_P.FXOS87006AxesSensor1_SampleTime;
  }

  status = 1U;
  status = MW_I2C_MasterWrite(SerialMaster_DW.obj_k.i2cobj.MW_I2C_HANDLE, 29U,
    &status, 1U, true, false);
  if (status == 0) {
    MW_I2C_MasterRead(SerialMaster_DW.obj_k.i2cobj.MW_I2C_HANDLE, 29U,
                      &output_raw[0], 6U, false, true);
    memcpy((void *)&SerialMaster_B.b_RegisterValue[0], (void *)&output_raw[0],
           (size_t)3 * sizeof(int16_T));
    memcpy((void *)&y[0], (void *)&SerialMaster_B.b_RegisterValue[0], (size_t)2 *
           sizeof(uint8_T));
    b_x[0] = y[1];
    b_x[1] = y[0];
    memcpy((void *)&SerialMaster_B.b_RegisterValue[0], (void *)&b_x[0], (size_t)
           1 * sizeof(int16_T));
    memcpy((void *)&y[0], (void *)&SerialMaster_B.b_RegisterValue[1], (size_t)2 *
           sizeof(uint8_T));
    b_x[0] = y[1];
    b_x[1] = y[0];
    memcpy((void *)&SerialMaster_B.b_RegisterValue[1], (void *)&b_x[0], (size_t)
           1 * sizeof(int16_T));
    memcpy((void *)&y[0], (void *)&SerialMaster_B.b_RegisterValue[2], (size_t)2 *
           sizeof(uint8_T));
    b_x[0] = y[1];
    b_x[1] = y[0];
    memcpy((void *)&SerialMaster_B.b_RegisterValue[2], (void *)&b_x[0], (size_t)
           1 * sizeof(int16_T));
  } else {
    SerialMaster_B.b_RegisterValue[0] = 0;
    SerialMaster_B.b_RegisterValue[1] = 0;
    SerialMaster_B.b_RegisterValue[2] = 0;
  }

  SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_0 = (real_T)
    (SerialMaster_B.b_RegisterValue[0] >> 2) * 2.0 * 0.244 / 1000.0;
  SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_1 = (real_T)
    (SerialMaster_B.b_RegisterValue[1] >> 2) * 2.0 * 0.244 / 1000.0;

  /* Sum: '<S4>/Subtract1' incorporates:
   *  Constant: '<S4>/Constant2'
   *  MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor1'
   * */
  SerialMaster_B.CastToDouble14 = (real_T)(SerialMaster_B.b_RegisterValue[2] >>
    2) * 2.0 * 0.244 / 1000.0 - SerialMaster_P.Constant2_Value_b;

  /* Sqrt: '<S4>/Square Root1' incorporates:
   *  Math: '<S4>/Square'
   *  Math: '<S4>/Square1'
   *  Math: '<S4>/Square2'
   *  Sum: '<S4>/Add'
   */
  SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_0 = sqrt
    ((SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_0 *
      SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_0 +
      SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_1 *
      SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_1) +
     SerialMaster_B.CastToDouble14 * SerialMaster_B.CastToDouble14);

  /* MATLABSystem: '<S4>/ ' */
  if (SerialMaster_DW.obj.TunablePropsChanged) {
    SerialMaster_DW.obj.TunablePropsChanged = false;
  }

  obj = SerialMaster_DW.obj.pStatistic;
  if (SerialMaster_DW.obj.pStatistic->isInitialized != 1) {
    SerialMaster_DW.obj.pStatistic->isSetupComplete = false;
    SerialMaster_DW.obj.pStatistic->isInitialized = 1;
    obj->pCumSum = 0.0;
    obj->pCumRevIndex = 1.0;
    obj->pModValueRev = 0.0;
    obj->isSetupComplete = true;
    obj->pCumSum = 0.0;
    for (i = 0; i < 299; i++) {
      obj->pCumSumRev[i] = 0.0;
      obj->pCumSumRev[i] = 0.0;
    }

    obj->pCumRevIndex = 1.0;
    obj->pModValueRev = 0.0;
  }

  SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_1 = obj->pCumRevIndex;
  SerialMaster_B.CastToDouble14 = obj->pCumSum;
  for (i = 0; i < 299; i++) {
    SerialMaster_B.csumrev[i] = obj->pCumSumRev[i];
  }

  SerialMaster_B.modValueRev = obj->pModValueRev;
  SerialMaster_B.z = 0.0;
  SerialMaster_B.rtb_u_m = 0.0;
  SerialMaster_B.CastToDouble14 += SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_0;
  if (SerialMaster_B.modValueRev == 0.0) {
    SerialMaster_B.z = SerialMaster_B.csumrev[(int32_T)
      SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_1 - 1] +
      SerialMaster_B.CastToDouble14;
  }

  SerialMaster_B.csumrev[(int32_T)SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_1
    - 1] = SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_0;
  if (SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_1 != 299.0) {
    SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_1++;
  } else {
    SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_1 = 1.0;
    SerialMaster_B.CastToDouble14 = 0.0;
    for (i = 297; i >= 0; i--) {
      SerialMaster_B.csumrev[i] += SerialMaster_B.csumrev[i + 1];
    }
  }

  if (SerialMaster_B.modValueRev == 0.0) {
    SerialMaster_B.rtb_u_m = SerialMaster_B.z / 300.0;
  }

  obj->pCumSum = SerialMaster_B.CastToDouble14;
  for (i = 0; i < 299; i++) {
    obj->pCumSumRev[i] = SerialMaster_B.csumrev[i];
  }

  obj->pCumRevIndex = SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_1;
  if (SerialMaster_B.modValueRev > 0.0) {
    obj->pModValueRev = SerialMaster_B.modValueRev - 1.0;
  } else {
    obj->pModValueRev = 0.0;
  }

  /* MATLAB Function: '<S4>/MATLAB Function' incorporates:
   *  Constant: '<S2>/on//off'
   *  DataTypeConversion: '<S2>/Cast To Double'
   *  DataTypeConversion: '<S2>/Cast To Double13'
   *  DataTypeConversion: '<S2>/Cast To Double14'
   *  DataTypeConversion: '<S2>/Cast To Double15'
   *  DataTypeConversion: '<S2>/Cast To Double2'
   *  Gain: '<S2>/Multiply10'
   *  Gain: '<S4>/Accel_Smooth'
   *  MATLABSystem: '<S4>/ '
   *  RelationalOperator: '<S2>/GreaterThan'
   *  UnitDelay: '<S4>/Unit Delay'
   */
  rtb_DigitalRead4_0 = !(SerialMaster_B.Mode >= SerialMaster_P.onoff_Value);
  if (rtb_DigitalRead4_0) {
    SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_0 = 0.0;
  } else {
    SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_0 =
      (SerialMaster_P.Accel_Smooth_Gain * SerialMaster_B.rtb_u_m - (real_T)
       SerialMaster_B.ActivityThreshold) * (10.0 * (real_T)
      SerialMaster_B.ResponseFactor) / (SerialMaster_P.Multiply10_Gain * (real_T)
      SerialMaster_B.RecoveryTime);
  }

  SerialMaster_DW.UnitDelay_DSTATE +=
    SerialMaster_B.rtb_FXOS87006AxesSensor1_idx_0 * 0.001;
  if (SerialMaster_DW.UnitDelay_DSTATE < SerialMaster_B.LRL) {
    SerialMaster_DW.UnitDelay_DSTATE = SerialMaster_B.LRL;
  } else if (SerialMaster_DW.UnitDelay_DSTATE > SerialMaster_B.MSR) {
    SerialMaster_DW.UnitDelay_DSTATE = SerialMaster_B.MSR;
  } else if (rtb_DigitalRead4_0) {
    SerialMaster_DW.UnitDelay_DSTATE = SerialMaster_B.LRL;
  }

  /* End of MATLAB Function: '<S4>/MATLAB Function' */

  /* Chart: '<Root>/PACEMAKER STATEFLOW' */
  if (SerialMaster_DW.temporalCounter_i1 < MAX_uint32_T) {
    SerialMaster_DW.temporalCounter_i1++;
  }

  if (SerialMaster_DW.is_active_c3_SerialMaster == 0U) {
    SerialMaster_DW.is_active_c3_SerialMaster = 1U;
    SerialMaster_DW.is_c3_SerialMaster = SerialMaster_IN_AOO;
    SerialMaster_DW.temporalCounter_i1 = 0U;
    SerialMaster_DW.is_AOO = SerialMaster_IN_Refractory;

    /* Update for UnitDelay: '<S4>/Unit Delay' */
    Seria_enter_atomic_Refractory_f(&SerialMaster_B.Product,
      &SerialMaster_DW.UnitDelay_DSTATE);
  } else {
    switch (SerialMaster_DW.is_c3_SerialMaster) {
     case SerialMaster_IN_AAI:
      /* Update for UnitDelay: '<S4>/Unit Delay' */
      SerialMaster_AAI(&SerialMaster_B.Multiply3, &SerialMaster_B.Product,
                       &SerialMaster_B.Multiply7, &SerialMaster_B.Product1,
                       &SerialMaster_DW.UnitDelay_DSTATE, &DigitalRead);
      break;

     case SerialMaster_IN_AOO:
      if ((SerialMaster_B.Mode == 2) || (SerialMaster_B.Mode == 6)) {
        SerialMaster_DW.is_AOO = SerialMaster_IN_NO_ACTIVE_CHILD;
        SerialMaster_DW.is_c3_SerialMaster = SerialMaster_IN_AAI;
        SerialMaster_DW.is_AAI = SerialMaster_IN_Refractory;

        /* Update for UnitDelay: '<S4>/Unit Delay' */
        SerialM_enter_atomic_Refractory(&SerialMaster_B.Product,
          &SerialMaster_DW.UnitDelay_DSTATE);
      } else if ((SerialMaster_B.Mode == 1) || (SerialMaster_B.Mode == 5)) {
        SerialMaster_DW.is_AOO = SerialMaster_IN_NO_ACTIVE_CHILD;
        SerialMaster_DW.is_c3_SerialMaster = SerialMaster_IN_VOO;
        SerialMaster_DW.temporalCounter_i1 = 0U;
        SerialMaster_DW.is_VOO = SerialMaster_IN_Refractory;

        /* Update for UnitDelay: '<S4>/Unit Delay' */
        Seri_enter_atomic_Refractory_f3(&SerialMaster_B.Product1,
          &SerialMaster_DW.UnitDelay_DSTATE);
      } else if ((SerialMaster_B.Mode == 3) || (SerialMaster_B.Mode == 7)) {
        SerialMaster_DW.is_AOO = SerialMaster_IN_NO_ACTIVE_CHILD;
        SerialMaster_DW.is_c3_SerialMaster = SerialMaster_IN_VVI;
        SerialMaster_DW.is_VVI = SerialMaster_IN_Refractory;

        /* Update for UnitDelay: '<S4>/Unit Delay' */
        Ser_enter_atomic_Refractory_f3x(&SerialMaster_B.Product1,
          &SerialMaster_DW.UnitDelay_DSTATE);
      } else if (SerialMaster_DW.is_AOO == SerialMaster_IN_Pace) {
        SerialMaster_B.D2_PACE_CHARGE_CTRL = 0.0;
        SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
        SerialMaster_B.D8_ATR_PACE_CTRL = 1.0;
        SerialMaster_B.D11_ATR_GND_CTRL = 0.0;
        SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
        SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
        SerialMaster_B.D12_VENT_GND_CTRL = 0.0;
        SerialMaster_B.D9_VENT_PACE_CTRL = 0.0;
        if (SerialMaster_DW.temporalCounter_i1 >= (uint32_T)ceil
            (SerialMaster_B.Multiply3)) {
          SerialMaster_DW.temporalCounter_i1 = 0U;
          SerialMaster_DW.is_AOO = SerialMaster_IN_Refractory;

          /* Update for UnitDelay: '<S4>/Unit Delay' */
          Seria_enter_atomic_Refractory_f(&SerialMaster_B.Product,
            &SerialMaster_DW.UnitDelay_DSTATE);
        }
      } else {
        /* case IN_Refractory: */
        SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
        SerialMaster_B.D9_VENT_PACE_CTRL = 0.0;
        SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
        SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
        SerialMaster_B.D8_ATR_PACE_CTRL = 0.0;
        SerialMaster_B.D11_ATR_GND_CTRL = 1.0;
        SerialMaster_B.D12_VENT_GND_CTRL = 0.0;
        SerialMaster_B.D2_PACE_CHARGE_CTRL = 1.0;
        if (SerialMaster_DW.temporalCounter_i1 >= (uint32_T)ceil
            (SerialMaster_DW.Standby_Period)) {
          SerialMaster_DW.temporalCounter_i1 = 0U;
          SerialMaster_DW.is_AOO = SerialMaster_IN_Pace;
          SerialMaster_B.D5_PACING_REF_PWM = 0.0;
          SerialMaster_B.D2_PACE_CHARGE_CTRL = 0.0;
          SerialMaster_B.D8_ATR_PACE_CTRL = 1.0;
          SerialMaster_B.D11_ATR_GND_CTRL = 0.0;
        }
      }
      break;

     case SerialMaster_IN_VOO:
      if ((SerialMaster_B.Mode == 0) || (SerialMaster_B.Mode == 4)) {
        SerialMaster_DW.is_VOO = SerialMaster_IN_NO_ACTIVE_CHILD;
        SerialMaster_DW.is_c3_SerialMaster = SerialMaster_IN_AOO;
        SerialMaster_DW.temporalCounter_i1 = 0U;
        SerialMaster_DW.is_AOO = SerialMaster_IN_Refractory;

        /* Update for UnitDelay: '<S4>/Unit Delay' */
        Seria_enter_atomic_Refractory_f(&SerialMaster_B.Product,
          &SerialMaster_DW.UnitDelay_DSTATE);
      } else if ((SerialMaster_B.Mode == 3) || (SerialMaster_B.Mode == 7)) {
        SerialMaster_DW.is_VOO = SerialMaster_IN_NO_ACTIVE_CHILD;
        SerialMaster_DW.is_c3_SerialMaster = SerialMaster_IN_VVI;
        SerialMaster_DW.is_VVI = SerialMaster_IN_Refractory;

        /* Update for UnitDelay: '<S4>/Unit Delay' */
        Ser_enter_atomic_Refractory_f3x(&SerialMaster_B.Product1,
          &SerialMaster_DW.UnitDelay_DSTATE);
      } else if ((SerialMaster_B.Mode == 2) || (SerialMaster_B.Mode == 6)) {
        SerialMaster_DW.is_VOO = SerialMaster_IN_NO_ACTIVE_CHILD;
        SerialMaster_DW.is_c3_SerialMaster = SerialMaster_IN_AAI;
        SerialMaster_DW.is_AAI = SerialMaster_IN_Refractory;

        /* Update for UnitDelay: '<S4>/Unit Delay' */
        SerialM_enter_atomic_Refractory(&SerialMaster_B.Product,
          &SerialMaster_DW.UnitDelay_DSTATE);
      } else if (SerialMaster_DW.is_VOO == SerialMaster_IN_Pace) {
        SerialMaster_B.D2_PACE_CHARGE_CTRL = 0.0;
        SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
        SerialMaster_B.D8_ATR_PACE_CTRL = 0.0;
        SerialMaster_B.D11_ATR_GND_CTRL = 0.0;
        SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
        SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
        SerialMaster_B.D12_VENT_GND_CTRL = 0.0;
        SerialMaster_B.D9_VENT_PACE_CTRL = 1.0;
        if (SerialMaster_DW.temporalCounter_i1 >= (uint32_T)ceil
            (SerialMaster_B.Multiply4)) {
          SerialMaster_DW.temporalCounter_i1 = 0U;
          SerialMaster_DW.is_VOO = SerialMaster_IN_Refractory;

          /* Update for UnitDelay: '<S4>/Unit Delay' */
          Seri_enter_atomic_Refractory_f3(&SerialMaster_B.Product1,
            &SerialMaster_DW.UnitDelay_DSTATE);
        }
      } else {
        /* case IN_Refractory: */
        SerialMaster_B.D10_PACE_GND_CTRL = 1.0;
        SerialMaster_B.D9_VENT_PACE_CTRL = 0.0;
        SerialMaster_B.D4_Z_ATR_CTRL = 0.0;
        SerialMaster_B.D7_Z_VENT_CTRL = 0.0;
        SerialMaster_B.D8_ATR_PACE_CTRL = 0.0;
        SerialMaster_B.D11_ATR_GND_CTRL = 0.0;
        SerialMaster_B.D12_VENT_GND_CTRL = 1.0;
        SerialMaster_B.D2_PACE_CHARGE_CTRL = 1.0;
        if (SerialMaster_DW.temporalCounter_i1 >= (uint32_T)ceil
            (SerialMaster_DW.Standby_Period)) {
          SerialMaster_DW.temporalCounter_i1 = 0U;
          SerialMaster_DW.is_VOO = SerialMaster_IN_Pace;
          SerialMaster_B.D5_PACING_REF_PWM = 0.0;
          SerialMaster_B.D2_PACE_CHARGE_CTRL = 0.0;
          SerialMaster_B.D12_VENT_GND_CTRL = 0.0;
          SerialMaster_B.D9_VENT_PACE_CTRL = 1.0;
        }
      }
      break;

     default:
      /* Update for UnitDelay: '<S4>/Unit Delay' */
      /* case IN_VVI: */
      SerialMaster_VVI(&SerialMaster_B.Product, &SerialMaster_B.Multiply4,
                       &SerialMaster_B.Multiply8, &SerialMaster_B.Product1,
                       &SerialMaster_DW.UnitDelay_DSTATE, &DigitalRead1);
      break;
    }
  }

  /* End of Chart: '<Root>/PACEMAKER STATEFLOW' */

  /* MATLABSystem: '<S1>/Digital Write2' */
  MW_digitalIO_write(SerialMaster_DW.obj_f.MW_DIGITALIO_HANDLE,
                     SerialMaster_B.D2_PACE_CHARGE_CTRL != 0.0);

  /* MATLABSystem: '<S1>/PWM Output2' */
  MW_PWM_SetDutyCycle(SerialMaster_DW.obj_ng.MW_PWM_HANDLE,
                      SerialMaster_B.D3_VENT_CMP_REF_PWM);

  /* MATLABSystem: '<S1>/Digital Write4' */
  MW_digitalIO_write(SerialMaster_DW.obj_n.MW_DIGITALIO_HANDLE,
                     SerialMaster_B.D4_Z_ATR_CTRL != 0.0);

  /* MATLABSystem: '<S1>/PWM Output' */
  MW_PWM_SetDutyCycle(SerialMaster_DW.obj_hj.MW_PWM_HANDLE,
                      SerialMaster_B.D5_PACING_REF_PWM);

  /* MATLABSystem: '<S1>/PWM Output1' */
  MW_PWM_SetDutyCycle(SerialMaster_DW.obj_nz.MW_PWM_HANDLE,
                      SerialMaster_B.D6_ATR_CMP_REF_PWM);

  /* MATLABSystem: '<S1>/Digital Write7' */
  MW_digitalIO_write(SerialMaster_DW.obj_d.MW_DIGITALIO_HANDLE,
                     SerialMaster_B.D7_Z_VENT_CTRL != 0.0);

  /* MATLABSystem: '<S1>/Digital Write8' */
  MW_digitalIO_write(SerialMaster_DW.obj_hc.MW_DIGITALIO_HANDLE,
                     SerialMaster_B.D8_ATR_PACE_CTRL != 0.0);

  /* MATLABSystem: '<S1>/Digital Write9' */
  MW_digitalIO_write(SerialMaster_DW.obj_kk.MW_DIGITALIO_HANDLE,
                     SerialMaster_B.D9_VENT_PACE_CTRL != 0.0);

  /* MATLABSystem: '<S1>/Digital Write10' */
  MW_digitalIO_write(SerialMaster_DW.obj_cw.MW_DIGITALIO_HANDLE,
                     SerialMaster_B.D10_PACE_GND_CTRL != 0.0);

  /* MATLABSystem: '<S1>/Digital Write11' */
  MW_digitalIO_write(SerialMaster_DW.obj_a.MW_DIGITALIO_HANDLE,
                     SerialMaster_B.D11_ATR_GND_CTRL != 0.0);

  /* MATLABSystem: '<S1>/Digital Write5' */
  MW_digitalIO_write(SerialMaster_DW.obj_g.MW_DIGITALIO_HANDLE,
                     SerialMaster_B.D12_VENT_GND_CTRL != 0.0);

  /* MATLABSystem: '<S1>/Digital Write6' */
  MW_digitalIO_write(SerialMaster_DW.obj_hx.MW_DIGITALIO_HANDLE,
                     SerialMaster_B.D13_FRONTEND_CONTROL);

  /* MATLABSystem: '<S2>/Digital Write' */
  MW_digitalIO_write(SerialMaster_DW.obj_e.MW_DIGITALIO_HANDLE,
                     SerialMaster_B.GreenLED);
}

/* Model initialize function */
void SerialMaster_initialize(void)
{
  {
    h_dsp_internal_SlidingWindowA_T *obj;
    int32_T i;

    /* InitializeConditions for UnitDelay: '<S4>/Unit Delay' */
    SerialMaster_DW.UnitDelay_DSTATE = SerialMaster_P.UnitDelay_InitialCondition;

    /* SystemInitialize for S-Function (sfun_private_function_caller) generated from: '<S2>/COM_OUT ' incorporates:
     *  SubSystem: '<S2>/COM_OUT '
     */
    send_DCM_Init();

    /* End of SystemInitialize for S-Function (sfun_private_function_caller) generated from: '<S2>/COM_OUT ' */

    /* SystemInitialize for Chart: '<Root>/PACEMAKER STATEFLOW' */
    SerialMaster_B.D13_FRONTEND_CONTROL = true;

    /* Start for MATLABSystem: '<S2>/Digital Read' */
    SerialMaster_DW.obj_c.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_c.SampleTime = SerialMaster_P.DigitalRead_SampleTime;
    SerialMaster_DW.obj_c.isInitialized = 1;
    SerialMaster_DW.obj_c.MW_DIGITALIO_HANDLE = MW_digitalIO_open(0U, 0);
    SerialMaster_DW.obj_c.isSetupComplete = true;

    /* Start for MATLABSystem: '<S2>/Digital Read1' */
    SerialMaster_DW.obj_bt.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_bt.SampleTime = SerialMaster_P.DigitalRead1_SampleTime;
    SerialMaster_DW.obj_bt.isInitialized = 1;
    SerialMaster_DW.obj_bt.MW_DIGITALIO_HANDLE = MW_digitalIO_open(1U, 0);
    SerialMaster_DW.obj_bt.isSetupComplete = true;

    /* Start for MATLABSystem: '<S2>/Serial Receive1' */
    SerialMaster_DW.obj_k3.isInitialized = 0;
    SerialMaster_DW.obj_k3.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_k3.SampleTime = SerialMaster_P.SerialReceive1_SampleTime;
    SerialMaster_SystemCore_setup_d(&SerialMaster_DW.obj_k3);

    /* Start for MATLABSystem: '<S2>/Digital Read4' */
    SerialMaster_DW.obj_h.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_h.SampleTime = SerialMaster_P.DigitalRead4_SampleTime;
    SerialMaster_DW.obj_h.isInitialized = 1;
    SerialMaster_DW.obj_h.MW_DIGITALIO_HANDLE = MW_digitalIO_open(16U, 0);
    SerialMaster_DW.obj_h.isSetupComplete = true;

    /* Start for MATLABSystem: '<S2>/Digital Read5' */
    SerialMaster_DW.obj_b.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_b.SampleTime = SerialMaster_P.DigitalRead5_SampleTime;
    SerialMaster_DW.obj_b.isInitialized = 1;
    SerialMaster_DW.obj_b.MW_DIGITALIO_HANDLE = MW_digitalIO_open(17U, 0);
    SerialMaster_DW.obj_b.isSetupComplete = true;

    /* Start for MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor1' */
    SerialMaster_DW.obj_k.isInitialized = 0;
    SerialMaster_DW.obj_k.i2cobj.isInitialized = 0;
    SerialMaster_DW.obj_k.i2cobj.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_k.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_k.SampleTime =
      SerialMaster_P.FXOS87006AxesSensor1_SampleTime;
    SerialMast_SystemCore_setup_drh(&SerialMaster_DW.obj_k);

    /* Start for MATLABSystem: '<S4>/ ' */
    SerialMaster_DW.obj.isInitialized = 0;
    SerialMaster_DW.obj.NumChannels = -1;
    SerialMaster_DW.obj.FrameLength = -1;
    SerialMaster_DW.obj.matlabCodegenIsDeleted = false;
    SerialMaste_SystemCore_setup_dr(&SerialMaster_DW.obj);

    /* InitializeConditions for MATLABSystem: '<S4>/ ' */
    obj = SerialMaster_DW.obj.pStatistic;
    if (obj->isInitialized == 1) {
      obj->pCumSum = 0.0;
      for (i = 0; i < 299; i++) {
        obj->pCumSumRev[i] = 0.0;
      }

      obj->pCumRevIndex = 1.0;
      obj->pModValueRev = 0.0;
    }

    /* End of InitializeConditions for MATLABSystem: '<S4>/ ' */

    /* Start for MATLABSystem: '<S1>/Digital Write2' */
    SerialMaster_DW.obj_f.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_f.isInitialized = 1;
    SerialMaster_DW.obj_f.MW_DIGITALIO_HANDLE = MW_digitalIO_open(2U, 1);
    SerialMaster_DW.obj_f.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/PWM Output2' */
    SerialMaster_DW.obj_ng.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_ng.isInitialized = 1;
    SerialMaster_DW.obj_ng.MW_PWM_HANDLE = MW_PWM_Open(3U, 2000.0, 0.0);
    MW_PWM_Start(SerialMaster_DW.obj_ng.MW_PWM_HANDLE);
    SerialMaster_DW.obj_ng.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/Digital Write4' */
    SerialMaster_DW.obj_n.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_n.isInitialized = 1;
    SerialMaster_DW.obj_n.MW_DIGITALIO_HANDLE = MW_digitalIO_open(4U, 1);
    SerialMaster_DW.obj_n.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/PWM Output' */
    SerialMaster_DW.obj_hj.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_hj.isInitialized = 1;
    SerialMaster_DW.obj_hj.MW_PWM_HANDLE = MW_PWM_Open(5U, 2000.0, 0.0);
    MW_PWM_Start(SerialMaster_DW.obj_hj.MW_PWM_HANDLE);
    SerialMaster_DW.obj_hj.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/PWM Output1' */
    SerialMaster_DW.obj_nz.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_nz.isInitialized = 1;
    SerialMaster_DW.obj_nz.MW_PWM_HANDLE = MW_PWM_Open(6U, 2000.0, 0.0);
    MW_PWM_Start(SerialMaster_DW.obj_nz.MW_PWM_HANDLE);
    SerialMaster_DW.obj_nz.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/Digital Write7' */
    SerialMaster_DW.obj_d.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_d.isInitialized = 1;
    SerialMaster_DW.obj_d.MW_DIGITALIO_HANDLE = MW_digitalIO_open(7U, 1);
    SerialMaster_DW.obj_d.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/Digital Write8' */
    SerialMaster_DW.obj_hc.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_hc.isInitialized = 1;
    SerialMaster_DW.obj_hc.MW_DIGITALIO_HANDLE = MW_digitalIO_open(8U, 1);
    SerialMaster_DW.obj_hc.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/Digital Write9' */
    SerialMaster_DW.obj_kk.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_kk.isInitialized = 1;
    SerialMaster_DW.obj_kk.MW_DIGITALIO_HANDLE = MW_digitalIO_open(9U, 1);
    SerialMaster_DW.obj_kk.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/Digital Write10' */
    SerialMaster_DW.obj_cw.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_cw.isInitialized = 1;
    SerialMaster_DW.obj_cw.MW_DIGITALIO_HANDLE = MW_digitalIO_open(10U, 1);
    SerialMaster_DW.obj_cw.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/Digital Write11' */
    SerialMaster_DW.obj_a.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_a.isInitialized = 1;
    SerialMaster_DW.obj_a.MW_DIGITALIO_HANDLE = MW_digitalIO_open(11U, 1);
    SerialMaster_DW.obj_a.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/Digital Write5' */
    SerialMaster_DW.obj_g.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_g.isInitialized = 1;
    SerialMaster_DW.obj_g.MW_DIGITALIO_HANDLE = MW_digitalIO_open(12U, 1);
    SerialMaster_DW.obj_g.isSetupComplete = true;

    /* Start for MATLABSystem: '<S1>/Digital Write6' */
    SerialMaster_DW.obj_hx.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_hx.isInitialized = 1;
    SerialMaster_DW.obj_hx.MW_DIGITALIO_HANDLE = MW_digitalIO_open(13U, 1);
    SerialMaster_DW.obj_hx.isSetupComplete = true;

    /* Start for MATLABSystem: '<S2>/Digital Write' */
    SerialMaster_DW.obj_e.matlabCodegenIsDeleted = false;
    SerialMaster_DW.obj_e.isInitialized = 1;
    SerialMaster_DW.obj_e.MW_DIGITALIO_HANDLE = MW_digitalIO_open(43U, 1);
    SerialMaster_DW.obj_e.isSetupComplete = true;
  }
}

/* Model terminate function */
void SerialMaster_terminate(void)
{
  b_freedomk64f_I2CMasterWrite__T *obj;
  h_dsp_internal_SlidingWindowA_T *obj_0;

  /* Terminate for MATLABSystem: '<S2>/Digital Read' */
  if (!SerialMaster_DW.obj_c.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_c.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_c.isInitialized == 1) &&
        SerialMaster_DW.obj_c.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_c.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Read' */

  /* Terminate for MATLABSystem: '<S2>/Digital Read1' */
  if (!SerialMaster_DW.obj_bt.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_bt.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_bt.isInitialized == 1) &&
        SerialMaster_DW.obj_bt.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_bt.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Read1' */

  /* Terminate for MATLABSystem: '<S2>/Serial Receive1' */
  if (!SerialMaster_DW.obj_k3.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_k3.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_k3.isInitialized == 1) &&
        SerialMaster_DW.obj_k3.isSetupComplete) {
      MW_SCI_Close(SerialMaster_DW.obj_k3.MW_SCIHANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Serial Receive1' */

  /* Terminate for MATLABSystem: '<S2>/Digital Read4' */
  if (!SerialMaster_DW.obj_h.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_h.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_h.isInitialized == 1) &&
        SerialMaster_DW.obj_h.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_h.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Read4' */

  /* Terminate for MATLABSystem: '<S2>/Digital Read5' */
  if (!SerialMaster_DW.obj_b.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_b.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_b.isInitialized == 1) &&
        SerialMaster_DW.obj_b.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_b.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Read5' */

  /* Terminate for S-Function (sfun_private_function_caller) generated from: '<S2>/COM_OUT ' incorporates:
   *  SubSystem: '<S2>/COM_OUT '
   */
  send_DCM_Term();

  /* End of Terminate for S-Function (sfun_private_function_caller) generated from: '<S2>/COM_OUT ' */

  /* Terminate for MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor1' */
  if (!SerialMaster_DW.obj_k.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_k.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_k.isInitialized == 1) &&
        SerialMaster_DW.obj_k.isSetupComplete) {
      MW_I2C_Close(SerialMaster_DW.obj_k.i2cobj.MW_I2C_HANDLE);
    }
  }

  obj = &SerialMaster_DW.obj_k.i2cobj;
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    if (obj->isInitialized == 1) {
      obj->isInitialized = 2;
    }
  }

  /* End of Terminate for MATLABSystem: '<S4>/FXOS8700 6-Axes Sensor1' */

  /* Terminate for MATLABSystem: '<S4>/ ' */
  if (!SerialMaster_DW.obj.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj.isInitialized == 1) &&
        SerialMaster_DW.obj.isSetupComplete) {
      obj_0 = SerialMaster_DW.obj.pStatistic;
      if (obj_0->isInitialized == 1) {
        obj_0->isInitialized = 2;
      }

      SerialMaster_DW.obj.NumChannels = -1;
      SerialMaster_DW.obj.FrameLength = -1;
    }
  }

  /* End of Terminate for MATLABSystem: '<S4>/ ' */

  /* Terminate for MATLABSystem: '<S1>/Digital Write2' */
  if (!SerialMaster_DW.obj_f.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_f.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_f.isInitialized == 1) &&
        SerialMaster_DW.obj_f.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_f.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/Digital Write2' */

  /* Terminate for MATLABSystem: '<S1>/PWM Output2' */
  if (!SerialMaster_DW.obj_ng.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_ng.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_ng.isInitialized == 1) &&
        SerialMaster_DW.obj_ng.isSetupComplete) {
      MW_PWM_Stop(SerialMaster_DW.obj_ng.MW_PWM_HANDLE);
      MW_PWM_Close(SerialMaster_DW.obj_ng.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/PWM Output2' */

  /* Terminate for MATLABSystem: '<S1>/Digital Write4' */
  if (!SerialMaster_DW.obj_n.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_n.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_n.isInitialized == 1) &&
        SerialMaster_DW.obj_n.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_n.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/Digital Write4' */

  /* Terminate for MATLABSystem: '<S1>/PWM Output' */
  if (!SerialMaster_DW.obj_hj.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_hj.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_hj.isInitialized == 1) &&
        SerialMaster_DW.obj_hj.isSetupComplete) {
      MW_PWM_Stop(SerialMaster_DW.obj_hj.MW_PWM_HANDLE);
      MW_PWM_Close(SerialMaster_DW.obj_hj.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/PWM Output' */

  /* Terminate for MATLABSystem: '<S1>/PWM Output1' */
  if (!SerialMaster_DW.obj_nz.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_nz.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_nz.isInitialized == 1) &&
        SerialMaster_DW.obj_nz.isSetupComplete) {
      MW_PWM_Stop(SerialMaster_DW.obj_nz.MW_PWM_HANDLE);
      MW_PWM_Close(SerialMaster_DW.obj_nz.MW_PWM_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/PWM Output1' */

  /* Terminate for MATLABSystem: '<S1>/Digital Write7' */
  if (!SerialMaster_DW.obj_d.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_d.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_d.isInitialized == 1) &&
        SerialMaster_DW.obj_d.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_d.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/Digital Write7' */

  /* Terminate for MATLABSystem: '<S1>/Digital Write8' */
  if (!SerialMaster_DW.obj_hc.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_hc.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_hc.isInitialized == 1) &&
        SerialMaster_DW.obj_hc.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_hc.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/Digital Write8' */

  /* Terminate for MATLABSystem: '<S1>/Digital Write9' */
  if (!SerialMaster_DW.obj_kk.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_kk.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_kk.isInitialized == 1) &&
        SerialMaster_DW.obj_kk.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_kk.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/Digital Write9' */

  /* Terminate for MATLABSystem: '<S1>/Digital Write10' */
  if (!SerialMaster_DW.obj_cw.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_cw.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_cw.isInitialized == 1) &&
        SerialMaster_DW.obj_cw.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_cw.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/Digital Write10' */

  /* Terminate for MATLABSystem: '<S1>/Digital Write11' */
  if (!SerialMaster_DW.obj_a.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_a.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_a.isInitialized == 1) &&
        SerialMaster_DW.obj_a.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_a.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/Digital Write11' */

  /* Terminate for MATLABSystem: '<S1>/Digital Write5' */
  if (!SerialMaster_DW.obj_g.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_g.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_g.isInitialized == 1) &&
        SerialMaster_DW.obj_g.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_g.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/Digital Write5' */

  /* Terminate for MATLABSystem: '<S1>/Digital Write6' */
  if (!SerialMaster_DW.obj_hx.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_hx.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_hx.isInitialized == 1) &&
        SerialMaster_DW.obj_hx.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_hx.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S1>/Digital Write6' */

  /* Terminate for MATLABSystem: '<S2>/Digital Write' */
  if (!SerialMaster_DW.obj_e.matlabCodegenIsDeleted) {
    SerialMaster_DW.obj_e.matlabCodegenIsDeleted = true;
    if ((SerialMaster_DW.obj_e.isInitialized == 1) &&
        SerialMaster_DW.obj_e.isSetupComplete) {
      MW_digitalIO_close(SerialMaster_DW.obj_e.MW_DIGITALIO_HANDLE);
    }
  }

  /* End of Terminate for MATLABSystem: '<S2>/Digital Write' */
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
