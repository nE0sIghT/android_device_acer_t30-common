# Copyright (C) 2012 The Android Open Source Project
# Copyright (C) 2014 The CyanogenMod Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import common

GSM_FILES = (
  "/system/priv-app/CellBroadcastReceiver",
  "/system/priv-app/Mms",
  "/system/priv-app/MmsService",
  "/system/app/Stk",
  "/system/app/WhisperPush",
  "/system/bin/rild",
  "/system/etc/acer_ril.db",
  "/system/etc/apns-conf.xml",
  "/system/etc/permissions/android.hardware.telephony.gsm.xml",
  "/system/etc/ppp/ip-up",
  "/system/etc/ppp/ip-down",
  "/system/etc/spn-conf.xml",
  "/system/lib/libcurve25519.so",
  "/system/lib/libhuawei-ril.so",
)

def FullOTA_InstallEnd(info):
  # Remove GSM-specific files on wifi-only device
  info.script.AppendExtra("if getprop(\"ro.boot.carrier\") == \"wifi-only\" then")
  info.script.Print("Removing GSM-specific files...")
  # TODO: We need to mount /system first
  DeleteFilesRecursive(info, GSM_FILES);
  info.script.AppendExtra("endif;")

def DeleteFilesRecursive(info, file_list):
  """Delete all files in file_list."""
  if not file_list: return
  cmd = "delete_recursive(" + ",\0".join(['"%s"' % (i,) for i in file_list]) + ");"
  info.script.AppendExtra(info.script._WordWrap(cmd))
