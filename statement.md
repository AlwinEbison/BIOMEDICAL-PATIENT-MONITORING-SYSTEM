# Project Statement: Biomedical Patient Monitoring System

## Problem Statement

Doctors and nurses check a patient's vital signs (like heart rate and temperature) many times a day. Checking each number by hand takes time, and it is easy to miss a wrong value. When there are many patients, it is also hard to tell who needs help first.

This project is a simple program that takes a patient's vital signs, checks if they are normal, gives a risk score, and shows which patient is in the most danger.

## Scope of the Project

The project can:

- Add new patients with their name, age and 4 vital signs (heart rate, oxygen level, temperature and breathing rate).
- Check each vital sign and mark it as LOW, HIGH or NORMAL.
- Give a risk score and a status like NORMAL, REQUIRES ATTENTION or HIGH ALERT.
- Show a report for one patient, a list of all patients, and the highest-risk patient.
- Reject wrong input like letters or negative numbers.

The project cannot:

- Save data after the program closes.
- Connect to real medical devices.
- Diagnose diseases or suggest treatment.
- Show a graphical screen. It runs in the terminal with a text menu.

## Target Users

- Nurses and ward staff
- Doctors
- Small clinics and home-care workers
- Students who want to learn how a patient monitoring system works

## High-Level Features

- Add a new patient
- Check vital signs
- Calculate risk score and status
- View a patient report
- Search for a patient by ID
- View all patients
- Find the highest-risk patient
- Check user input so the program does not crash