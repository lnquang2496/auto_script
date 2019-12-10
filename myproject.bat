@echo off
call cls
call set PCL_PATH=D:\
REM call set PCL_PATH=D:\repo\s920\trunk\_project\06_Test_Specification\02_UnitTest\INT_V3H_PA_19027_B

REM /* IMR State ******************************************************************************/

REM call set PCL_NAME=IMR_INT_V3H_B_V1_unit_test_specification_imr_state.xlsx
REM call set TP_DIR=ut_imr_state
REM call set CANTATA_DIR=D:\UT_workspace\%TP_DIR%\Cantata\tests

REM call set SRC_NAME=r_imr_state_mng
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_imr_set --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_imr_get --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_imr_lock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_imr_unlock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM call set SRC_NAME=r_imr_rtt_state_mng
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_rtt_set --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_rtt_get --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_rtt_lock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_rtt_unlock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_rtt_get_channel --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM /* IMR Kernel *****************************************************************************/

REM call set PCL_NAME=IMR_INT_V3H_B_V1_unit_test_specification_imr_driver.xlsx
REM call set TP_DIR=ut_imr_driver
REM call set CANTATA_DIR=D:\UT_workspace\%TP_DIR%\Cantata\tests

REM This component need to copy from backup
REM call set SRC_NAME=r_imr_drvknl
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_init_devtree --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_interrupt_handler --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_init_channel  --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_read_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_write_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_init --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_init_core --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_read_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_write_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_write_status --source %SRC_NAME% --check_seq Trmyue --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_interrupt_notify --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_set_cpg_state --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_get_cpg_state --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_reset_cpg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM /* IMR OSAL ******************************************************************************/

REM call set PCL_NAME=IMR_INT_V3H_B_V1_unit_test_specification_imr_osal.xlsx
REM call set TP_DIR=ut_imr_osal
REM call set CANTATA_DIR=D:\UT_workspace\%TP_DIR%\Cantata\tests

REM call set SRC_NAME=r_imr_osal_ctl
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_init --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_deinit --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_start --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_stop --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_get_iodevice --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM call set SRC_NAME=r_imr_osal_msg
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_msg_del --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_msg_task_entry --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_msg_timeout_task --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_msg_receive --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_msg_timeout_wait --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM call set SRC_NAME=r_imr_osal_sem
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_init_devtree --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_sem_lock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_sem_unlock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM call set SRC_NAME=r_imr_osal_io
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_init_devtree --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_io_ctl_set_cpg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_io_ctl_read_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_io_ctl_write_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM /* IMR API *****************************************************************************/

call set PCL_NAME=pcl_imr_api_quangla.xlsx
REM call set PCL_NAME=IMR_INT_V3H_B_V1_unit_test_specification_imr_api.xlsx
call set TP_DIR=ut_imr_api_new
REM call set TP_DIR=ut_imr_api_re_execute
call set CANTATA_DIR=D:\UT_workspace\%TP_DIR%\Cantata\tests

REM call set SRC_NAME=r_imr_drvapi_ctl
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_Init --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_Deinit --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_Start --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_Stop --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_Open --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_Close --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_GetVersion --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM call set SRC_NAME=r_imr_drvapi_conf
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SetSource --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SoftwareReset --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SetMipmapMaxlod --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SetMipmapMemory --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_ControlCache --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_software_reset --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM call set SRC_NAME=r_imr_drvapi_conf_v3h
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SelectFilteringPipeline --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SetSyncModule --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SetRSExtMemory --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_EnableRotatorScaler --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_get_rsofr_ofm_val --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

call set SRC_NAME=r_imr_dlapi_ins
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlNop --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlTrap --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlWtl --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlWtl2 --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlWts --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlInt --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlSyncm --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlGosub --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlRet --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

call set SRC_NAME=r_imr_dlapi_ins_v3h
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlWup --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlSlp --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlStrect --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlOutnor --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlOutrot --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlSynccc --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlSynccf --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM call set SRC_NAME=r_imr_drvapi_exe
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_ExecuteExt --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_WaitEvent --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_WaitEventTimeout --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_init_info --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_get_reg_exe --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_get_cmrcr_efpe --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_get_cmrcr --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_check_dl --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_check_src --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_check_dst --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_wait_event --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_get_precision --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

call set SRC_NAME=r_imr_dlapi_ctl
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_CreateDl --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DestroyDl --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_ClearDl --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_RewindDl --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

call set SRC_NAME=r_imr_dlapi_coor
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_CoordinateTransform --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SetDstClippingArea --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_FillRect --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DlTri --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_dlapi_check_rect_param --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

call set SRC_NAME=r_imr_dlapi_cmn
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_dlapi_check_dl_param --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_dlapi_add_operand --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main_2.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_dlapi_memset --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM call set SRC_NAME=r_imr_drvapi_rtt_sp
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_rtt_chk_reg_val --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_rtt_chk_write_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_rtt_set_clock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
