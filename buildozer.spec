[app]
title = Digital Clock
package.name = digitalclock
package.domain = org.example

source.dir = .
source.include_exts = py,kv,png,jpg,atlas

version = 1.0.0
requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a, armeabi-v7a
android.minapi = 23
android.accept_sdk_license = True
android.debug_artifact = apk

[buildozer]
log_level = 2
warn_on_root = 0
