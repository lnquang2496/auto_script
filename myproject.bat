@echo off
call cls
call set PCL_PATH=D:\auto_script_asil\auto_script
call set PCL_NAME=OSAL_PCL.xlsx
call set CAN_WP=C:\Users\quangla\workspace\test_imr_ut\Cantata\tests
if exist output del /q output

call python reset_stub_instance.py --can_dir %CAN_WP% --source r_imr_osal_ctl

call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_init --source r_imr_osal_ctl --check_seq False --can_dir %CAN_WP%
call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_deinit --source r_imr_osal_ctl --check_seq False --can_dir %CAN_WP%
call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_start --source r_imr_osal_ctl --check_seq True --can_dir %CAN_WP%
call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_stop --source r_imr_osal_ctl --check_seq True --can_dir %CAN_WP%
call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_osal_ctl_get_iodevice --source r_imr_osal_ctl --check_seq True --can_dir %CAN_WP%

REM copy test_r_imr_osal_ctl_start.h %CAN_WP%\test_r_imr_osal_ctl\test_r_imr_osal_ctl_start.h
REM del /q test_r_imr_osal_ctl_start.h