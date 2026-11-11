#!/bin/bash
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus
exec /opt/google/chrome/chrome --user-data-dir=.home/agent/.config/google-chrome-cdp   --remote-debugging-port=9222 --no-first-run --disable-session-crashed-bubble   "https://www.mixamo.com/#/"
