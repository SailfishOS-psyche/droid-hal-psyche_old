# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device psyche
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Xiaomi 12X
%define rpm_device psyche
%define installable_zip 1

%define enable_kernel_update 1
%define enable_dtbo_update 1
%define enable_vendor_boot_update 1

%define droid_target_aarch64 1

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

# want adreno quirks is required for browser at least, and other subtle issues
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%define straggler_files \
   /bugreports \
   /cache \
   /d \
   /sdcard \
%{nil}

# Using droid-system instead of mounting
%define makefstab_skip_entries /product /system /system_ext /vendor /odm
Requires: droid-system

# Custom Firmware mount
Requires: custom_firmware
%define makefstab_skip_entries /vendor/bt_firmware /vendor/dsp /vendor/firmware_mnt

%include rpm/dhd/droid-hal-device.inc
