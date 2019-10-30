@echo off
call cls
call set PCL_PATH=D:\auto_script_asil\auto_script
call set PCL_NAME=KERNEL_PCL.xlsx
call set CAN_WP=C:\Users\quangla\workspace\test_pcl_script_1\Cantata\tests
call set KERNEL_SRC=r_imr_drvknl
if exist output del /q output

call python reset_stub_instance.py --can_dir %CAN_WP% --source %KERNEL_SRC%

call python myproject.py --idir %PCL_PATH% --ifile %PCL_NAME% --wsheet r_imr_drvknl_init_devtree --source %KERNEL_SRC% --check_seq True --can_dir %CAN_WP%
