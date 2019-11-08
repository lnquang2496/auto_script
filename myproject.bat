@echo off
call cls
call set PCL_PATH=D:\repo\rss2_rivp_tech\trunk\doc\tech\imr_int_b\04_UTP

REM call set PCL_NAME=IMR_INT_V3H_B_V1_unit_test_specification_imr_Kernel.xlsx
REM call set TP_DIR=UTP_IMR_driver_kernel
REM call set CANTATA_DIR=C:\Users\quangla\workspace\%TP_DIR%\Cantata\tests

REM call set SRC_NAME=r_imr_drvknl
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_init_devtree --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_init_channel --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_init --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_init_core --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_read_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_write_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_iodev_write_status --source %SRC_NAME% --check_seq Trmyue --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_interrupt_handler --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_read_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_write_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

call set PCL_NAME=IMR_INT_V3H_B_V1_unit_test_specification_imr_State.xlsx
call set TP_DIR=UTP_IMR_State_Management
call set CANTATA_DIR=C:\Users\quangla\workspace\%TP_DIR%\Cantata\tests

call set SRC_NAME=r_imr_state_mng
call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
call python combine.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_imr_set --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_imr_set --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_imr_get --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_imr_lock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_imr_unlock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM call set SRC_NAME=r_imr_rtt_state_mng
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_rtt_set --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_rtt_get --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_rtt_lock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_rtt_unlock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_state_rtt_get_channel --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM call set PCL_NAME=IMR_INT_V3H_B_V1_unit_test_specification_imr_OSAL.xlsx
REM call set TP_DIR=UTP_IMR_OSAL
REM call set CANTATA_DIR=C:\Users\quangla\workspace\%TP_DIR%\Cantata\tests

REM call set SRC_NAME=r_imr_osal_ctl
REM call python fixed_part.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python test.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_sem_lock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_init --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_deinit --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_start --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_stop --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_get_iodevice --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM call set SRC_NAME=r_imr_osal_msg
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_msg_del --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_msg_task_entry --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_msg_timeout_task --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_msg_receive --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_msg_timeout_wait --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM call set SRC_NAME=r_imr_osal_sem
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_sem_lock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_sem_unlock --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%

REM call set SRC_NAME=r_imr_osal_io
REM call python reset_stub_instance.py --can_dir %CANTATA_DIR% --source %SRC_NAME%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_io_ctl_set_cpg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_io_ctl_read_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
REM call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_io_ctl_write_reg --source %SRC_NAME% --check_seq True --can_dir %CANTATA_DIR%
