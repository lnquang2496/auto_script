@echo off
call cls
call set PCL_PATH=D:\repo\rss2_rivp_tech\trunk\doc\tech\imr_int_b\04_UTP

REM /* IMR State ******************************************************************************/
REM call set PCL_NAME=IMR_INT_V3H_B_V1_unit_test_specification_imr_State.xlsx
REM call set TP_DIR=UTP_IMR_State
REM call set CANTATA_DIR=C:\Users\quangla\workspace\%TP_DIR%\Cantata\tests

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

REM call set PCL_NAME=IMR_INT_V3H_B_V1_unit_test_specification_imr_Kernel.xlsx
REM call set TP_DIR=UTP_IMR_Kernel
REM call set CANTATA_DIR=C:\Users\quangla\workspace\%TP_DIR%\Cantata\tests

REM call set SRC_NAME=r_imr_drvknl
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_init_devtree --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_init_channel --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_init --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_init_core --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_read_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_write_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_write_status --source %SRC_NAME% --check_seq Trmyue --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_interrupt_handler --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_read_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_write_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM /* IMR OSAL ******************************************************************************/

REM call set PCL_NAME=IMR_INT_V3H_B_V1_unit_test_specification_imr_OSAL.xlsx
REM call set TP_DIR=UTP_IMR_OSAL
REM call set CANTATA_DIR=C:\Users\quangla\workspace\%TP_DIR%\Cantata\tests

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

call set PCL_NAME=IMR_INT_V3H_B_V1_unit_test_specification_imr_API.xlsx
call set TP_DIR=UTP_IMR_API
call set CANTATA_DIR=C:\Users\quangla\workspace\%TP_DIR%\Cantata\tests

call set SRC_NAME=r_imr_drvapi_ctl
call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_Init --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_Deinit --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_Start --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_Stop --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_Open --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_Close --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_GetVersion --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

call set SRC_NAME=r_imr_drvapi_conf
call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SetSource --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SoftwareReset --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SetMipmapMaxlod --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SetMipmapMemory --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_ControlCache --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_software_reset --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

call set SRC_NAME=r_imr_drvapi_conf_v3h
call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SelectFilteringPipeline --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SetSyncModule --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_SetRSExtMemory --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_EnableRotatorScaler --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_get_rsofr_ofm_val --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%





call set SRC_NAME=r_imr_dlapi_ctl
call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_CreateDl --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_DestroyDl --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_ClearDl --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet R_IMR_RewindDl --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

call set SRC_NAME=r_imr_drvapi_rtt_sp
call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
call python create_memdump.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet no_use --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_rtt_chk_reg_val --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_rtt_chk_write_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
call python main.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvapi_rtt_set_clock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

