#!/usr/bin/env python3

import Settings
import GALoop

settings = Settings.Settings()
ga_loop = GALoop.GALoop(settings)
ga_loop.loop()
