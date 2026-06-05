# Skill: detect-clicks

## Description
NBHF (Narrow-Band High-Frequency) click detection for finless porpoise acoustic data.
Specialized for Yangtze finless porpoise clicks (center frequency: 110-150 kHz).

## Trigger
- User mentions: click, pulse, NBHF, PAM, acoustic detection
- Research phase: Phase 2 (Data Analysis)

## Input
- Required: audio_path (str) - path to .wav or .flac file
- Optional:
  - threshold_db (float, default -134.0) - SPL detection threshold
  - bandpass_low (float, default 100000) - low frequency cutoff (Hz)
  - bandpass_high (float, default 180000) - high frequency cutoff (Hz)

## Steps
1. Load and validate audio (sr >= 500 kHz required for NBHF)
2. Apply Butterworth bandpass filter (100-180 kHz, 4th order)
3. Detect pulses using SPL threshold
4. Extract click trains using ICI pattern matching
5. Extract 18+ features (time, spectral, energy)
6. Classify: regular_click / buzz / noise / vessel_noise

## Decision Points
- If SNR < 3 dB: flag as low-confidence
- If buzz_ratio > 0.3: indicate active feeding
- If FPR > 10%: suggest threshold adjustment

## References
- Akamatsu et al. (2005). JASA
- Kimura et al. (2010). JASA
- Fang et al. (2015). JASA
