# Linux Security Monitoring & Automation Lab

A Python-based security monitoring tool that analyzes authentication logs, identifies repeated failed login attempts, and generates a structured security report.

## Overview

This project was created as a hands-on cybersecurity lab to practice Linux security concepts, Python programming, log analysis, pattern matching, and basic security-event detection.

The tool analyzes a controlled authentication log, extracts failed and successful login events, identifies source IP addresses associated with failed authentication attempts, and flags sources that exceed a configurable threshold.

## Features

- Authentication log analysis
- Failed and successful login detection
- Source IP address extraction
- Failed-attempt aggregation
- Potential brute-force activity detection
- Configurable detection threshold
- JSON security report generation
- Error handling for missing log files
- Automated analysis timing

## Technologies

- Python 3
- Linux/Unix concepts
- Bash
- Regular Expressions
- JSON
- Git & GitHub

## Project Structure

```text
linux-security-monitor/
├── auth.log
├── security_monitor.py
├── security_report.json
└── README.md


How It Works

The program follows a basic security-monitoring pipeline:

Authentication Log
       ↓
Read Log Entries
       ↓
Identify Authentication Events
       ↓
Extract Source IP Addresses
       ↓
Count Failed Attempts
       ↓
Apply Detection Threshold
       ↓
Generate Security Report


Usage

Run the monitoring tool with:

python3 security_monitor.py

Example output:

==================================================
Linux Security Monitoring Tool
==================================================

Security Event Summary
--------------------------------------------------
Failed login attempts: 7
Successful login attempts: 2
Unique source addresses: 2

Potential Brute-Force Activity
--------------------------------------------------
192.168.1.25: 5 failed attempts

Analysis duration: 0.0004 seconds
JSON report saved to: security_report.json

Analysis complete.
Detection Logic

The project uses a configurable threshold to identify repeated failed authentication attempts.

BRUTE_FORCE_THRESHOLD = 3

A source IP address with three or more failed login attempts is reported as a potential brute-force source.

The tool does not automatically classify an event as an attack. Repeated failed authentication attempts are treated as indicators that may require further investigation.

Security Concepts Demonstrated
Authentication monitoring
Security log analysis
Brute-force detection concepts
IP address analysis
Regular expression pattern matching
Event aggregation
Security automation
Structured security reporting
Linux security fundamentals
Lab Environment

The authentication log used in this project is a controlled, simulated dataset created for educational purposes.

No unauthorized systems or production authentication logs were accessed.

Future Improvements

Potential improvements include:

Command-line arguments for custom log files
Configurable detection thresholds
Timestamp-based event analysis
CSV report generation
Real-time log monitoring
Email or alert integration
Integration with security monitoring platforms
Visualization of authentication events
Ethical Use

This project is intended for educational purposes and authorized security testing only.

Do not use security monitoring or analysis tools against systems, accounts, or networks without appropriate authorization.