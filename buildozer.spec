[app]
# (str) Title of your application
title = Touchless Gesture Navigator

# (str) Package name
package.name = touchlessgesture

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (str) List of inclusions using pattern matching
source.include_exts = py,kv,png,txt

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3, kivy==2.3.0, opencv-python, mediapipe, numpy

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (str) Presplash of the application
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (str) Supported source code encoding
source.encoding = utf-8

# (list) List of whitelist patterns to include
# (default is to include all files when source.include_exts is set)
# include_patterns = assets/*,images/*.png

# (str) Application entry point, if not main.py
# entrypoint = main.py

# (int) Android API to use
android.api = 33

# (int) Minimum Android API supported
android.minapi = 24

# (str) Android NDK version
android.ndk = 25b

# (str) Android SDK version
# android.sdk = 33

# (list) Android architectures to build for
android.archs = armeabi-v7a, arm64-v8a

# (list) Permissions
android.permissions = CAMERA,INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,WAKE_LOCK,ACCESS_NETWORK_STATE,VIBRATE

# (str) Android entry point, default is org.kivy.android.PythonActivity
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, leave blank for default
# android.theme = '@style/Theme.Kivy'

# (list) Android Java classes to add to the final package
# android.add_jars = classes.jar

# (list) Android .aar dependencies
# android.add_aars = some-library.aar

# (str) Extra buildozer arguments
# buildozer.extra_args = --private

# (str) Enable Android log output in buildozer
log_level = 2

# (str) Application permissions inside manifest
# android.manifest_application_attributes = android:debuggable="true"

# (str) Additional manifest XML to include
# android.manifest_xml = <queries>...</queries>

# (str) Should buildozer use the Python3 recipe (default)?
# Use python3 only to support the app on modern Android.

[buildozer]
# (str) Path to buildozer executable if not on PATH
# buildozer = /usr/local/bin/buildozer

# (int) Number of concurrent jobs when building
# jobs = 4

# (str) Android SDK directory (if needed)
# android.sdk_path = /path/to/android/sdk

# (str) Android NDK directory (if needed)
# android.ndk_path = /path/to/android/ndk

# (str) Python-for-Android checkout directory
# p4a.source_dir = /path/to/python-for-android

# (bool) Skip windows support if this is not available
# windows.enable = 0
