import streamlit as st
import pandas as pd
import numpy as np
import math

# Page setup
st.set_page_config(page_title="MIAA D1 Football Tracker & Playoff Predictor", layout="wide", page_icon="🏈")

st.title("🏈 MIAA Division 1 Football Leaderboard & Playoff Simulator")
st.caption("Official MIAA Ratings & Standings (As of October 27) • Playoff Bracket, Chronological Schedules & Math Predictor")

# --- 1. FULL 33-TEAM DIVISION 1 DATABASE WITH DATED SCHEDULES ---
teams_data = {
    "St. John's Prep": {
        "record": "7-0", "wins": 7, "losses": 0, "rating": 27.7980, "avg_margin": 12.5714, "opp_rating": 15.2266, "seed": 1,
        "schedule": [
            {"date": "2026-09-11", "opp": "Barnstable", "loc": "Home", "result": "W", "score_us": 35, "score_them": 7, "cap": 14},
            {"date": "2026-09-18", "opp": "Central Catholic", "loc": "Away", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-09-25", "opp": "La Salle (R.I.)", "loc": "Home", "result": "W", "score_us": 42, "score_them": 13, "cap": 14},
            {"date": "2026-10-03", "opp": "Saint John's", "loc": "Home", "result": "W", "score_us": 43, "score_them": 20, "cap": 14},
            {"date": "2026-10-10", "opp": "Boston College High", "loc": "Away", "result": "W", "score_us": 38, "score_them": 7, "cap": 14},
            {"date": "2026-10-17", "opp": "Catholic Memorial", "loc": "Home", "result": "W", "score_us": 35, "score_them": 21, "cap": 14},
            {"date": "2026-10-23", "opp": "Malden Catholic", "loc": "Home", "result": "W", "score_us": 31, "score_them": 12, "cap": 14},
            {"date": "2026-10-30", "opp": "Catholic Memorial", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Saint John's (Shrewsbury)": {
        "record": "6-1", "wins": 6, "losses": 1, "rating": 25.9005, "avg_margin": 10.0000, "opp_rating": 15.9005, "seed": 2,
        "schedule": [
            {"date": "2026-09-11", "opp": "Mansfield", "loc": "Home", "result": "W", "score_us": 31, "score_them": 14, "cap": 14},
            {"date": "2026-09-18", "opp": "Leominster", "loc": "Home", "result": "W", "score_us": 35, "score_them": 10, "cap": 14},
            {"date": "2026-09-25", "opp": "Shrewsbury", "loc": "Away", "result": "W", "score_us": 42, "score_them": 7, "cap": 14},
            {"date": "2026-10-03", "opp": "St. John's Prep", "loc": "Away", "result": "L", "score_us": 20, "score_them": 43, "cap": -14},
            {"date": "2026-10-09", "opp": "BC High", "loc": "Home", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-10-17", "opp": "Algonquin", "loc": "Home", "result": "W", "score_us": 27, "score_them": 18, "cap": 9},
            {"date": "2026-10-23", "opp": "Catholic Memorial", "loc": "Home", "result": "W", "score_us": 34, "score_them": 7, "cap": 14},
            {"date": "2026-10-30", "opp": "BC High", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Central Catholic": {
        "record": "4-3", "wins": 4, "losses": 3, "rating": 23.6116, "avg_margin": 3.4286, "opp_rating": 20.1831, "seed": 3,
        "schedule": [
            {"date": "2026-09-11", "opp": "Springfield Central", "loc": "Away", "result": "L", "score_us": 14, "score_them": 35, "cap": -14},
            {"date": "2026-09-18", "opp": "St. John's Prep", "loc": "Home", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-09-25", "opp": "Methuen", "loc": "Home", "result": "W", "score_us": 31, "score_them": 14, "cap": 14},
            {"date": "2026-10-02", "opp": "Lowell", "loc": "Away", "result": "W", "score_us": 35, "score_them": 7, "cap": 14},
            {"date": "2026-10-09", "opp": "Londonderry (NH)", "loc": "Home", "result": "L", "score_us": 27, "score_them": 28, "cap": -1},
            {"date": "2026-10-16", "opp": "Lawrence", "loc": "Away", "result": "W", "score_us": 42, "score_them": 0, "cap": 14},
            {"date": "2026-10-23", "opp": "Andover", "loc": "Away", "result": "W", "score_us": 42, "score_them": 24, "cap": 14},
            {"date": "2026-10-29", "opp": "Haverhill", "loc": "Home", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Springfield Central": {
        "record": "6-1", "wins": 6, "losses": 1, "rating": 20.5456, "avg_margin": 9.0000, "opp_rating": 11.5456, "seed": 4,
        "schedule": [
            {"date": "2026-09-11", "opp": "Central Catholic", "loc": "Home", "result": "W", "score_us": 35, "score_them": 14, "cap": 14},
            {"date": "2026-09-18", "opp": "Iona Prep (NY)", "loc": "Away", "result": "L", "score_us": 20, "score_them": 28, "cap": -8},
            {"date": "2026-09-25", "opp": "Minnechaug", "loc": "Home", "result": "W", "score_us": 42, "score_them": 7, "cap": 14},
            {"date": "2026-10-02", "opp": "Westfield", "loc": "Away", "result": "W", "score_us": 40, "score_them": 12, "cap": 14},
            {"date": "2026-10-09", "opp": "East Longmeadow", "loc": "Home", "result": "W", "score_us": 55, "score_them": 14, "cap": 14},
            {"date": "2026-10-16", "opp": "Chicopee Comp", "loc": "Away", "result": "W", "score_us": 49, "score_them": 0, "cap": 14},
            {"date": "2026-10-23", "opp": "West Springfield", "loc": "Home", "result": "W", "score_us": 42, "score_them": 14, "cap": 14},
            {"date": "2026-10-30", "opp": "West Springfield", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Wachusett Regional": {
        "record": "7-0", "wins": 7, "losses": 0, "rating": 20.2372, "avg_margin": 11.0000, "opp_rating": 9.2372, "seed": 5,
        "schedule": [
            {"date": "2026-09-11", "opp": "Fitchburg", "loc": "Home", "result": "W", "score_us": 42, "score_them": 6, "cap": 14},
            {"date": "2026-09-18", "opp": "Shepherd Hill", "loc": "Away", "result": "W", "score_us": 35, "score_them": 0, "cap": 14},
            {"date": "2026-09-25", "opp": "Shrewsbury", "loc": "Home", "result": "W", "score_us": 28, "score_them": 7, "cap": 14},
            {"date": "2026-10-02", "opp": "Marlborough", "loc": "Away", "result": "W", "score_us": 31, "score_them": 10, "cap": 14},
            {"date": "2026-10-09", "opp": "Westborough", "loc": "Home", "result": "W", "score_us": 42, "score_them": 0, "cap": 14},
            {"date": "2026-10-16", "opp": "Leominster", "loc": "Away", "result": "W", "score_us": 21, "score_them": 14, "cap": 7},
            {"date": "2026-10-23", "opp": "Grafton", "loc": "Away", "result": "W", "score_us": 38, "score_them": 0, "cap": 14},
            {"date": "2026-10-30", "opp": "Algonquin", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Xaverian Brothers": {
        "record": "3-4", "wins": 3, "losses": 4, "rating": 17.7758, "avg_margin": -0.2857, "opp_rating": 18.0616, "seed": 6,
        "schedule": [
            {"date": "2026-09-11", "opp": "Everett", "loc": "Home", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-09-18", "opp": "Central Catholic", "loc": "Away", "result": "L", "score_us": 14, "score_them": 21, "cap": -7},
            {"date": "2026-09-25", "opp": "Springfield Central", "loc": "Home", "result": "L", "score_us": 17, "score_them": 31, "cap": -14},
            {"date": "2026-10-02", "opp": "Brockton", "loc": "Away", "result": "W", "score_us": 35, "score_them": 7, "cap": 14},
            {"date": "2026-10-09", "opp": "St. John's Prep", "loc": "Away", "result": "L", "score_us": 14, "score_them": 35, "cap": -14},
            {"date": "2026-10-16", "opp": "Catholic Memorial", "loc": "Home", "result": "L", "score_us": 21, "score_them": 42, "cap": -14},
            {"date": "2026-10-23", "opp": "BC High", "loc": "Away", "result": "W", "score_us": 47, "score_them": 6, "cap": 14},
            {"date": "2026-10-30", "opp": "Malden Catholic", "loc": "Home", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Andover": {
        "record": "5-2", "wins": 5, "losses": 2, "rating": 16.3508, "avg_margin": 3.7143, "opp_rating": 12.6365, "seed": 7,
        "schedule": [
            {"date": "2026-09-11", "opp": "Lincoln-Sudbury", "loc": "Home", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-09-18", "opp": "Methuen", "loc": "Away", "result": "W", "score_us": 35, "score_them": 21, "cap": 14},
            {"date": "2026-09-25", "opp": "Billerica", "loc": "Home", "result": "W", "score_us": 24, "score_them": 14, "cap": 10},
            {"date": "2026-10-02", "opp": "North Andover", "loc": "Away", "result": "W", "score_us": 31, "score_them": 7, "cap": 14},
            {"date": "2026-10-09", "opp": "Pinkerton (NH)", "loc": "Home", "result": "W", "score_us": 36, "score_them": 29, "cap": 7},
            {"date": "2026-10-16", "opp": "Lowell", "loc": "Away", "result": "L", "score_us": 14, "score_them": 21, "cap": -7},
            {"date": "2026-10-23", "opp": "Central Catholic", "loc": "Home", "result": "L", "score_us": 24, "score_them": 42, "cap": -14},
            {"date": "2026-10-30", "opp": "Tewksbury", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Franklin": {
        "record": "5-2", "wins": 5, "losses": 2, "rating": 16.0439, "avg_margin": 5.4286, "opp_rating": 10.6153, "seed": 8,
        "schedule": [
            {"date": "2026-09-11", "opp": "Waltham", "loc": "Home", "result": "W", "score_us": 28, "score_them": 7, "cap": 14},
            {"date": "2026-09-18", "opp": "Taunton", "loc": "Away", "result": "W", "score_us": 31, "score_them": 14, "cap": 14},
            {"date": "2026-09-25", "opp": "King Philip", "loc": "Home", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-10-02", "opp": "North Attleborough", "loc": "Away", "result": "W", "score_us": 24, "score_them": 10, "cap": 14},
            {"date": "2026-10-09", "opp": "Milton", "loc": "Away", "result": "L", "score_us": 6, "score_them": 41, "cap": -14},
            {"date": "2026-10-16", "opp": "Attleboro", "loc": "Home", "result": "W", "score_us": 21, "score_them": 6, "cap": 14},
            {"date": "2026-10-23", "opp": "Milton", "loc": "Away", "result": "L", "score_us": 6, "score_them": 41, "cap": -14},
            {"date": "2026-10-30", "opp": "Taunton", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Leominster": {
        "record": "4-3", "wins": 4, "losses": 3, "rating": 15.3921, "avg_margin": 3.2857, "opp_rating": 12.1064, "seed": 9,
        "schedule": [
            {"date": "2026-09-11", "opp": "Doherty", "loc": "Home", "result": "W", "score_us": 35, "score_them": 14, "cap": 14},
            {"date": "2026-09-18", "opp": "Saint John's", "loc": "Away", "result": "L", "score_us": 10, "score_them": 35, "cap": -14},
            {"date": "2026-09-25", "opp": "Algonquin", "loc": "Home", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-10-02", "opp": "Grafton", "loc": "Away", "result": "L", "score_us": 14, "score_them": 21, "cap": -7},
            {"date": "2026-10-09", "opp": "Shrewsbury", "loc": "Home", "result": "W", "score_us": 40, "score_them": 21, "cap": 14},
            {"date": "2026-10-16", "opp": "Wachusett", "loc": "Home", "result": "L", "score_us": 14, "score_them": 21, "cap": -7},
            {"date": "2026-10-23", "opp": "Westborough", "loc": "Home", "result": "W", "score_us": 21, "score_them": 7, "cap": 14},
            {"date": "2026-10-30", "opp": "Grafton", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Brockton": {
        "record": "3-4", "wins": 3, "losses": 4, "rating": 10.8963, "avg_margin": -1.7143, "opp_rating": 12.6106, "seed": 10,
        "schedule": [
            {"date": "2026-09-11", "opp": "BC High", "loc": "Home", "result": "W", "score_us": 21, "score_them": 14, "cap": 7},
            {"date": "2026-09-18", "opp": "Natick", "loc": "Away", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-09-25", "opp": "Bridgewater-Raynham", "loc": "Home", "result": "L", "score_us": 7, "score_them": 24, "cap": -14},
            {"date": "2026-10-02", "opp": "Xaverian", "loc": "Home", "result": "L", "score_us": 7, "score_them": 35, "cap": -14},
            {"date": "2026-10-09", "opp": "Weymouth", "loc": "Away", "result": "W", "score_us": 21, "score_them": 8, "cap": 13},
            {"date": "2026-10-16", "opp": "Durfee", "loc": "Home", "result": "L", "score_us": 14, "score_them": 21, "cap": -7},
            {"date": "2026-10-24", "opp": "New Bedford", "loc": "Home", "result": "L", "score_us": 14, "score_them": 20, "cap": -6},
            {"date": "2026-10-30", "opp": "Durfee", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Natick": {
        "record": "4-3", "wins": 4, "losses": 3, "rating": 10.8125, "avg_margin": 2.1429, "opp_rating": 8.6697, "seed": 11,
        "schedule": [
            {"date": "2026-09-11", "opp": "Needham", "loc": "Home", "result": "W", "score_us": 24, "score_them": 7, "cap": 14},
            {"date": "2026-09-18", "opp": "Brockton", "loc": "Home", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-09-25", "opp": "Walpole", "loc": "Away", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-10-02", "opp": "Milton", "loc": "Home", "result": "L", "score_us": 10, "score_them": 24, "cap": -14},
            {"date": "2026-10-09", "opp": "Newton North", "loc": "Home", "result": "W", "score_us": 37, "score_them": 14, "cap": 14},
            {"date": "2026-10-16", "opp": "Brookline", "loc": "Away", "result": "W", "score_us": 27, "score_them": 6, "cap": 14},
            {"date": "2026-10-23", "opp": "Wellesley", "loc": "Home", "result": "W", "score_us": 37, "score_them": 14, "cap": 14},
            {"date": "2026-10-30", "opp": "Walpole", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Haverhill": {
        "record": "5-2", "wins": 5, "losses": 2, "rating": 10.6868, "avg_margin": 6.0000, "opp_rating": 4.6868, "seed": 12,
        "schedule": [
            {"date": "2026-09-11", "opp": "Beverly", "loc": "Home", "result": "W", "score_us": 28, "score_them": 7, "cap": 14},
            {"date": "2026-09-18", "opp": "Lowell", "loc": "Home", "result": "W", "score_us": 35, "score_them": 14, "cap": 14},
            {"date": "2026-09-25", "opp": "Chelmsford", "loc": "Away", "result": "W", "score_us": 24, "score_them": 10, "cap": 14},
            {"date": "2026-10-02", "opp": "Lawrence", "loc": "Home", "result": "W", "score_us": 42, "score_them": 0, "cap": 14},
            {"date": "2026-10-09", "opp": "Methuen", "loc": "Home", "result": "W", "score_us": 40, "score_them": 34, "cap": 6},
            {"date": "2026-10-16", "opp": "New Bedford", "loc": "Home", "result": "L", "score_us": 28, "score_them": 34, "cap": -6},
            {"date": "2026-10-23", "opp": "Methuen", "loc": "Home", "result": "W", "score_us": 40, "score_them": 34, "cap": 6},
            {"date": "2026-10-29", "opp": "Central Catholic", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "New Bedford": {
        "record": "6-1", "wins": 6, "losses": 1, "rating": 10.4183, "avg_margin": 7.2857, "opp_rating": 3.1326, "seed": 13,
        "schedule": [
            {"date": "2026-09-11", "opp": "Durfee", "loc": "Home", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-09-18", "opp": "Barnstable", "loc": "Away", "result": "W", "score_us": 31, "score_them": 17, "cap": 14},
            {"date": "2026-09-25", "opp": "Bridgewater-Raynham", "loc": "Away", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-10-02", "opp": "Taunton", "loc": "Home", "result": "W", "score_us": 24, "score_them": 7, "cap": 14},
            {"date": "2026-10-09", "opp": "Haverhill", "loc": "Away", "result": "W", "score_us": 34, "score_them": 28, "cap": 6},
            {"date": "2026-10-16", "opp": "Attleboro", "loc": "Home", "result": "W", "score_us": 27, "score_them": 14, "cap": 13},
            {"date": "2026-10-24", "opp": "Brockton", "loc": "Away", "result": "W", "score_us": 20, "score_them": 14, "cap": 6},
            {"date": "2026-10-30", "opp": "Dartmouth", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Everett": {
        "record": "6-1", "wins": 6, "losses": 1, "rating": 10.3895, "avg_margin": 5.7143, "opp_rating": 4.6752, "seed": 14,
        "schedule": [
            {"date": "2026-09-11", "opp": "Xaverian", "loc": "Away", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-09-18", "opp": "BC High", "loc": "Home", "result": "W", "score_us": 21, "score_them": 14, "cap": 7},
            {"date": "2026-09-25", "opp": "Somerville", "loc": "Home", "result": "W", "score_us": 35, "score_them": 7, "cap": 14},
            {"date": "2026-10-02", "opp": "Malden", "loc": "Away", "result": "W", "score_us": 42, "score_them": 0, "cap": 14},
            {"date": "2026-10-09", "opp": "Lynn English", "loc": "Home", "result": "W", "score_us": 35, "score_them": 12, "cap": 14},
            {"date": "2026-10-16", "opp": "Revere", "loc": "Away", "result": "W", "score_us": 28, "score_them": 7, "cap": 14},
            {"date": "2026-10-23", "opp": "Somerville", "loc": "Home", "result": "W", "score_us": 27, "score_them": 26, "cap": 1},
            {"date": "2026-10-30", "opp": "Lynn Classical", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Newton North": {
        "record": "6-1", "wins": 6, "losses": 1, "rating": 6.8728, "avg_margin": 6.7143, "opp_rating": 0.1585, "seed": 15,
        "schedule": [
            {"date": "2026-09-10", "opp": "Waltham", "loc": "Home", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-09-18", "opp": "Newton South", "loc": "Home", "result": "W", "score_us": 20, "score_them": 14, "cap": 6},
            {"date": "2026-09-25", "opp": "Weymouth", "loc": "Away", "result": "W", "score_us": 14, "score_them": 12, "cap": 2},
            {"date": "2026-10-02", "opp": "Framingham", "loc": "Home", "result": "W", "score_us": 29, "score_them": 18, "cap": 11},
            {"date": "2026-10-09", "opp": "Natick", "loc": "Away", "result": "L", "score_us": 14, "score_them": 37, "cap": -14},
            {"date": "2026-10-16", "opp": "Wellesley", "loc": "Home", "result": "W", "score_us": 31, "score_them": 6, "cap": 14},
            {"date": "2026-10-23", "opp": "Cumberland (R.I.)", "loc": "Away", "result": "W", "score_us": 26, "score_them": 7, "cap": 14},
            {"date": "2026-10-30", "opp": "Braintree", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Weymouth": {
        "record": "5-2", "wins": 5, "losses": 2, "rating": 6.5816, "avg_margin": 4.5714, "opp_rating": 2.0102, "seed": 16,
        "schedule": [
            {"date": "2026-09-11", "opp": "Braintree", "loc": "Home", "result": "W", "score_us": 28, "score_them": 7, "cap": 14},
            {"date": "2026-09-18", "opp": "Milton", "loc": "Away", "result": "L", "score_us": 7, "score_them": 28, "cap": -14},
            {"date": "2026-09-25", "opp": "Newton North", "loc": "Home", "result": "L", "score_us": 12, "score_them": 14, "cap": -2},
            {"date": "2026-10-02", "opp": "Wellesley", "loc": "Away", "result": "W", "score_us": 24, "score_them": 10, "cap": 14},
            {"date": "2026-10-09", "opp": "Brockton", "loc": "Home", "result": "L", "score_us": 8, "score_them": 21, "cap": -13},
            {"date": "2026-10-16", "opp": "Framingham", "loc": "Away", "result": "W", "score_us": 27, "score_them": 14, "cap": 13},
            {"date": "2026-10-23", "opp": "Needham", "loc": "Away", "result": "W", "score_us": 33, "score_them": 15, "cap": 14},
            {"date": "2026-10-29", "opp": "Milton", "loc": "Home", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Methuen": {
        "record": "2-5", "wins": 2, "losses": 5, "rating": 8.8828, "avg_margin": -4.8571, "opp_rating": 13.7399, "seed": 17,
        "schedule": [
            {"date": "2026-09-11", "opp": "Central Catholic", "loc": "Away", "result": "L", "score_us": 14, "score_them": 31, "cap": -14},
            {"date": "2026-09-18", "opp": "Andover", "loc": "Home", "result": "L", "score_us": 21, "score_them": 35, "cap": -14},
            {"date": "2026-09-25", "opp": "Lowell", "loc": "Away", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-10-02", "opp": "North Andover", "loc": "Home", "result": "L", "score_us": 10, "score_them": 24, "cap": -14},
            {"date": "2026-10-09", "opp": "Haverhill", "loc": "Away", "result": "L", "score_us": 34, "score_them": 40, "cap": -6},
            {"date": "2026-10-16", "opp": "Lawrence", "loc": "Home", "result": "W", "score_us": 42, "score_them": 12, "cap": 14},
            {"date": "2026-10-23", "opp": "Haverhill", "loc": "Away", "result": "L", "score_us": 34, "score_them": 40, "cap": -6},
            {"date": "2026-10-30", "opp": "Billerica", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Shrewsbury": {
        "record": "3-4", "wins": 3, "losses": 4, "rating": 8.5019, "avg_margin": -4.4286, "opp_rating": 12.9305, "seed": 18,
        "schedule": [
            {"date": "2026-09-11", "opp": "Algonquin", "loc": "Away", "result": "W", "score_us": 24, "score_them": 10, "cap": 14},
            {"date": "2026-09-18", "opp": "Wachusett", "loc": "Away", "result": "L", "score_us": 7, "score_them": 28, "cap": -14},
            {"date": "2026-09-25", "opp": "Saint John's", "loc": "Home", "result": "L", "score_us": 7, "score_them": 42, "cap": -14},
            {"date": "2026-10-02", "opp": "Westborough", "loc": "Home", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-10-09", "opp": "Leominster", "loc": "Away", "result": "L", "score_us": 21, "score_them": 40, "cap": -14},
            {"date": "2026-10-16", "opp": "Grafton", "loc": "Home", "result": "L", "score_us": 14, "score_them": 21, "cap": -7},
            {"date": "2026-10-24", "opp": "Algonquin", "loc": "Home", "result": "W", "score_us": 27, "score_them": 18, "cap": 9},
            {"date": "2026-10-30", "opp": "Westborough", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Boston College High": {
        "record": "1-6", "wins": 1, "losses": 6, "rating": 8.2511, "avg_margin": -8.7143, "opp_rating": 16.9654, "seed": 19,
        "schedule": [
            {"date": "2026-09-11", "opp": "Brockton", "loc": "Away", "result": "L", "score_us": 14, "score_them": 21, "cap": -7},
            {"date": "2026-09-18", "opp": "Everett", "loc": "Away", "result": "L", "score_us": 14, "score_them": 21, "cap": -7},
            {"date": "2026-09-25", "opp": "Catholic Memorial", "loc": "Home", "result": "L", "score_us": 7, "score_them": 35, "cap": -14},
            {"date": "2026-10-02", "opp": "St. John's Prep", "loc": "Home", "result": "L", "score_us": 7, "score_them": 38, "cap": -14},
            {"date": "2026-10-09", "opp": "Saint John's", "loc": "Away", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-10-17", "opp": "Malden Catholic", "loc": "Home", "result": "W", "score_us": 22, "score_them": 10, "cap": 12},
            {"date": "2026-10-23", "opp": "Xaverian", "loc": "Home", "result": "L", "score_us": 6, "score_them": 47, "cap": -14},
            {"date": "2026-10-30", "opp": "Saint John's", "loc": "Home", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Lowell": {
        "record": "2-5", "wins": 2, "losses": 5, "rating": 6.1900, "avg_margin": -4.2857, "opp_rating": 10.4757, "seed": 20,
        "schedule": [
            {"date": "2026-09-11", "opp": "Methuen", "loc": "Home", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-09-18", "opp": "Haverhill", "loc": "Away", "result": "L", "score_us": 14, "score_them": 35, "cap": -14},
            {"date": "2026-09-25", "opp": "Chelmsford", "loc": "Home", "result": "W", "score_us": 21, "score_them": 14, "cap": 7},
            {"date": "2026-10-02", "opp": "Central Catholic", "loc": "Home", "result": "L", "score_us": 7, "score_them": 35, "cap": -14},
            {"date": "2026-10-09", "opp": "Andover", "loc": "Home", "result": "W", "score_us": 21, "score_them": 14, "cap": 7},
            {"date": "2026-10-16", "opp": "Billerica", "loc": "Away", "result": "L", "score_us": 18, "score_them": 41, "cap": -14},
            {"date": "2026-10-23", "opp": "Lawrence", "loc": "Away", "result": "W", "score_us": 46, "score_them": 0, "cap": 14},
            {"date": "2026-10-30", "opp": "North Andover", "loc": "Home", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Framingham": {
        "record": "4-3", "wins": 4, "losses": 3, "rating": 4.3554, "avg_margin": 0.5714, "opp_rating": 3.7840, "seed": 21,
        "schedule": [
            {"date": "2026-09-11", "opp": "Newton North", "loc": "Away", "result": "L", "score_us": 18, "score_them": 29, "cap": -11},
            {"date": "2026-09-18", "opp": "Brookline", "loc": "Home", "result": "W", "score_us": 21, "score_them": 14, "cap": 7},
            {"date": "2026-09-25", "opp": "Needham", "loc": "Away", "result": "W", "score_us": 24, "score_them": 14, "cap": 10},
            {"date": "2026-10-02", "opp": "Natick", "loc": "Away", "result": "L", "score_us": 7, "score_them": 28, "cap": -14},
            {"date": "2026-10-09", "opp": "Weymouth", "loc": "Home", "result": "L", "score_us": 14, "score_them": 27, "cap": -13},
            {"date": "2026-10-16", "opp": "Durfee", "loc": "Home", "result": "W", "score_us": 28, "score_them": 27, "cap": 1},
            {"date": "2026-10-23", "opp": "Durfee", "loc": "Home", "result": "W", "score_us": 28, "score_them": 27, "cap": 1},
            {"date": "2026-10-30", "opp": "Needham", "loc": "Home", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Taunton": {
        "record": "3-4", "wins": 3, "losses": 4, "rating": 4.0806, "avg_margin": -1.2857, "opp_rating": 5.3663, "seed": 22,
        "schedule": [
            {"date": "2026-09-11", "opp": "Stoughton", "loc": "Home", "result": "W", "score_us": 21, "score_them": 8, "cap": 13},
            {"date": "2026-09-18", "opp": "Franklin", "loc": "Home", "result": "L", "score_us": 14, "score_them": 31, "cap": -14},
            {"date": "2026-09-25", "opp": "Mansfield", "loc": "Away", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-10-02", "opp": "New Bedford", "loc": "Away", "result": "L", "score_us": 7, "score_them": 24, "cap": -14},
            {"date": "2026-10-09", "opp": "North Attleborough", "loc": "Home", "result": "W", "score_us": 24, "score_them": 14, "cap": 10},
            {"date": "2026-10-17", "opp": "Stoughton", "loc": "Away", "result": "W", "score_us": 21, "score_them": 8, "cap": 13},
            {"date": "2026-10-23", "opp": "Attleboro", "loc": "Away", "result": "L", "score_us": 20, "score_them": 27, "cap": -7},
            {"date": "2026-10-30", "opp": "Franklin", "loc": "Home", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Durfee": {
        "record": "5-2", "wins": 5, "losses": 2, "rating": 3.9070, "avg_margin": 6.2857, "opp_rating": -2.3787, "seed": 23,
        "schedule": [
            {"date": "2026-09-11", "opp": "New Bedford", "loc": "Away", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-09-18", "opp": "Dartmouth", "loc": "Home", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-09-25", "opp": "TechBoston", "loc": "Home", "result": "W", "score_us": 35, "score_them": 0, "cap": 14},
            {"date": "2026-10-02", "opp": "Brockton", "loc": "Away", "result": "W", "score_us": 21, "score_them": 14, "cap": 7},
            {"date": "2026-10-09", "opp": "Framingham", "loc": "Away", "result": "L", "score_us": 27, "score_them": 28, "cap": -1},
            {"date": "2026-10-16", "opp": "Brockton", "loc": "Away", "result": "W", "score_us": 21, "score_them": 14, "cap": 7},
            {"date": "2026-10-23", "opp": "TechBoston", "loc": "Away", "result": "W", "score_us": 34, "score_them": 7, "cap": 14},
            {"date": "2026-10-30", "opp": "Brockton", "loc": "Home", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Attleboro": {
        "record": "3-4", "wins": 3, "losses": 4, "rating": 3.1732, "avg_margin": -3.2857, "opp_rating": 6.4589, "seed": 24,
        "schedule": [
            {"date": "2026-09-11", "opp": "Milford", "loc": "Home", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-09-18", "opp": "North Attleborough", "loc": "Away", "result": "W", "score_us": 21, "score_them": 14, "cap": 7},
            {"date": "2026-09-25", "opp": "King Philip", "loc": "Away", "result": "L", "score_us": 7, "score_them": 35, "cap": -14},
            {"date": "2026-10-02", "opp": "Mansfield", "loc": "Home", "result": "L", "score_us": 14, "score_them": 21, "cap": -7},
            {"date": "2026-10-09", "opp": "New Bedford", "loc": "Away", "result": "L", "score_us": 14, "score_them": 27, "cap": -13},
            {"date": "2026-10-16", "opp": "Franklin", "loc": "Away", "result": "L", "score_us": 6, "score_them": 21, "cap": -14},
            {"date": "2026-10-23", "opp": "Taunton", "loc": "Home", "result": "W", "score_us": 27, "score_them": 20, "cap": 7},
            {"date": "2026-10-30", "opp": "Milford", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Acton-Boxborough": {
        "record": "3-3", "wins": 3, "losses": 3, "rating": 3.0709, "avg_margin": 0.5000, "opp_rating": 2.5709, "seed": 25,
        "schedule": [
            {"date": "2026-09-11", "opp": "Bedford", "loc": "Home", "result": "W", "score_us": 24, "score_them": 14, "cap": 10},
            {"date": "2026-09-18", "opp": "Weston", "loc": "Away", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-09-25", "opp": "Lincoln-Sudbury", "loc": "Home", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-10-02", "opp": "Wayland", "loc": "Away", "result": "L", "score_us": 30, "score_them": 47, "cap": -14},
            {"date": "2026-10-09", "opp": "Waltham", "loc": "Home", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-10-23", "opp": "Waltham", "loc": "Away", "result": "W", "score_us": 35, "score_them": 13, "cap": 14},
            {"date": "2026-10-30", "opp": "Bedford", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Needham": {
        "record": "1-6", "wins": 1, "losses": 6, "rating": 2.7401, "avg_margin": -8.7143, "opp_rating": 11.4544, "seed": 26,
        "schedule": [
            {"date": "2026-09-11", "opp": "Natick", "loc": "Away", "result": "L", "score_us": 7, "score_them": 24, "cap": -14},
            {"date": "2026-09-18", "opp": "Framingham", "loc": "Home", "result": "L", "score_us": 14, "score_them": 24, "cap": -10},
            {"date": "2026-09-25", "opp": "Milton", "loc": "Away", "result": "L", "score_us": 7, "score_them": 35, "cap": -14},
            {"date": "2026-10-02", "opp": "Wellesley", "loc": "Home", "result": "L", "score_us": 10, "score_them": 21, "cap": -11},
            {"date": "2026-10-09", "opp": "Braintree", "loc": "Home", "result": "W", "score_us": 21, "score_them": 7, "cap": 14},
            {"date": "2026-10-16", "opp": "Weymouth", "loc": "Home", "result": "L", "score_us": 15, "score_them": 33, "cap": -14},
            {"date": "2026-10-23", "opp": "Weymouth", "loc": "Home", "result": "L", "score_us": 15, "score_them": 33, "cap": -14},
            {"date": "2026-10-30", "opp": "Framingham", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Arlington": {
        "record": "2-5", "wins": 2, "losses": 5, "rating": 0.1879, "avg_margin": -3.8571, "opp_rating": 4.0451, "seed": 27,
        "schedule": [
            {"date": "2026-09-11", "opp": "Woburn", "loc": "Away", "result": "L", "score_us": 7, "score_them": 21, "cap": -14},
            {"date": "2026-09-18", "opp": "Reading", "loc": "Home", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-09-25", "opp": "Belmont", "loc": "Away", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-10-02", "opp": "Lexington", "loc": "Home", "result": "W", "score_us": 35, "score_them": 0, "cap": 14},
            {"date": "2026-10-09", "opp": "Winchester", "loc": "Home", "result": "L", "score_us": 14, "score_them": 38, "cap": -14},
            {"date": "2026-10-16", "opp": "Woburn", "loc": "Home", "result": "L", "score_us": 0, "score_them": 7, "cap": -7},
            {"date": "2026-10-23", "opp": "Woburn", "loc": "Home", "result": "L", "score_us": 0, "score_them": 7, "cap": -7},
            {"date": "2026-10-30", "opp": "Lexington", "loc": "Home", "result": "W (Forfeit)", "score_us": 2, "score_them": 0, "cap": 2}
        ]
    },
    "Brookline": {
        "record": "3-4", "wins": 3, "losses": 4, "rating": -1.7666, "avg_margin": -3.5714, "opp_rating": 1.8049, "seed": 28,
        "schedule": [
            {"date": "2026-09-11", "opp": "Wellesley", "loc": "Home", "result": "W", "score_us": 21, "score_them": 14, "cap": 7},
            {"date": "2026-09-18", "opp": "Framingham", "loc": "Away", "result": "L", "score_us": 14, "score_them": 21, "cap": -7},
            {"date": "2026-09-25", "opp": "Braintree", "loc": "Home", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-10-02", "opp": "Newton South", "loc": "Away", "result": "W", "score_us": 24, "score_them": 14, "cap": 10},
            {"date": "2026-10-09", "opp": "Natick", "loc": "Away", "result": "L", "score_us": 6, "score_them": 27, "cap": -14},
            {"date": "2026-10-16", "opp": "Natick", "loc": "Home", "result": "L", "score_us": 6, "score_them": 27, "cap": -14},
            {"date": "2026-10-23", "opp": "Natick", "loc": "Home", "result": "L", "score_us": 6, "score_them": 27, "cap": -14},
            {"date": "2026-10-30", "opp": "Wellesley", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Lawrence": {
        "record": "1-6", "wins": 1, "losses": 6, "rating": -3.8168, "avg_margin": -10.2857, "opp_rating": 6.4689, "seed": 29,
        "schedule": [
            {"date": "2026-09-11", "opp": "Lowell", "loc": "Away", "result": "L", "score_us": 0, "score_them": 46, "cap": -14},
            {"date": "2026-09-18", "opp": "Chelmsford", "loc": "Home", "result": "L", "score_us": 7, "score_them": 35, "cap": -14},
            {"date": "2026-09-25", "opp": "North Andover", "loc": "Away", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-10-02", "opp": "Haverhill", "loc": "Away", "result": "L", "score_us": 0, "score_them": 42, "cap": -14},
            {"date": "2026-10-09", "opp": "Methuen", "loc": "Home", "result": "L", "score_us": 12, "score_them": 42, "cap": -14},
            {"date": "2026-10-16", "opp": "Central Catholic", "loc": "Home", "result": "L", "score_us": 0, "score_them": 42, "cap": -14},
            {"date": "2026-10-23", "opp": "Lowell", "loc": "Home", "result": "L", "score_us": 0, "score_them": 46, "cap": -14},
            {"date": "2026-10-30", "opp": "Chelmsford", "loc": "Home", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Braintree": {
        "record": "1-6", "wins": 1, "losses": 6, "rating": -5.6503, "avg_margin": -10.8571, "opp_rating": 5.2069, "seed": 30,
        "schedule": [
            {"date": "2026-09-11", "opp": "Weymouth", "loc": "Away", "result": "L", "score_us": 7, "score_them": 28, "cap": -14},
            {"date": "2026-09-18", "opp": "Wellesley", "loc": "Home", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-09-25", "opp": "Brookline", "loc": "Away", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-10-02", "opp": "Milton", "loc": "Home", "result": "L", "score_us": 6, "score_them": 41, "cap": -14},
            {"date": "2026-10-09", "opp": "Needham", "loc": "Away", "result": "L", "score_us": 7, "score_them": 21, "cap": -14},
            {"date": "2026-10-16", "opp": "Walpole", "loc": "Home", "result": "L", "score_us": 7, "score_them": 48, "cap": -14},
            {"date": "2026-10-23", "opp": "Walpole", "loc": "Home", "result": "L", "score_us": 7, "score_them": 48, "cap": -14},
            {"date": "2026-10-30", "opp": "Newton North", "loc": "Home", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Newton South": {
        "record": "1-6", "wins": 1, "losses": 6, "rating": -6.9349, "avg_margin": -7.0000, "opp_rating": 0.0651, "seed": 31,
        "schedule": [
            {"date": "2026-09-11", "opp": "Weston", "loc": "Home", "result": "L", "score_us": 14, "score_them": 35, "cap": -14},
            {"date": "2026-09-18", "opp": "Newton North", "loc": "Away", "result": "L", "score_us": 14, "score_them": 20, "cap": -6},
            {"date": "2026-09-25", "opp": "Waltham", "loc": "Home", "result": "L", "score_us": 7, "score_them": 28, "cap": -14},
            {"date": "2026-10-02", "opp": "Brookline", "loc": "Home", "result": "L", "score_us": 14, "score_them": 24, "cap": -10},
            {"date": "2026-10-09", "opp": "Cambridge", "loc": "Home", "result": "L", "score_us": 20, "score_them": 21, "cap": -1},
            {"date": "2026-10-16", "opp": "Boston Latin", "loc": "Away", "result": "W", "score_us": 28, "score_them": 14, "cap": 14},
            {"date": "2026-10-23", "opp": "Cambridge", "loc": "Home", "result": "L", "score_us": 20, "score_them": 21, "cap": -1},
            {"date": "2026-10-30", "opp": "Westford", "loc": "Away", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Belmont": {
        "record": "2-5", "wins": 2, "losses": 5, "rating": -10.3076, "avg_margin": -7.1429, "opp_rating": -3.1647, "seed": 32,
        "schedule": [
            {"date": "2026-09-11", "opp": "Woburn", "loc": "Home", "result": "L", "score_us": 0, "score_them": 49, "cap": -14},
            {"date": "2026-09-18", "opp": "Reading", "loc": "Away", "result": "L", "score_us": 0, "score_them": 41, "cap": -14},
            {"date": "2026-09-25", "opp": "Arlington", "loc": "Home", "result": "L", "score_us": 14, "score_them": 28, "cap": -14},
            {"date": "2026-10-02", "opp": "Lexington", "loc": "Away", "result": "W", "score_us": 28, "score_them": 0, "cap": 14},
            {"date": "2026-10-09", "opp": "Winchester", "loc": "Away", "result": "L", "score_us": 7, "score_them": 35, "cap": -14},
            {"date": "2026-10-16", "opp": "Watertown", "loc": "Home", "result": "W", "score_us": 21, "score_them": 14, "cap": 7},
            {"date": "2026-10-23", "opp": "Reading", "loc": "Away", "result": "L", "score_us": 0, "score_them": 41, "cap": -14},
            {"date": "2026-10-30", "opp": "Winchester", "loc": "Home", "result": "TBD", "score_us": None, "score_them": None, "cap": 0}
        ]
    },
    "Lexington": {
        "record": "0-7", "wins": 0, "losses": 7, "rating": -13.5601, "avg_margin": -14.0000, "opp_rating": 0.4399, "seed": 33,
        "schedule": [
            {"date": "2026-09-11", "opp": "Reading", "loc": "Away", "result": "L", "score_us": 0, "score_them": 62, "cap": -14},
            {"date": "2026-09-18", "opp": "Woburn", "loc": "Home", "result": "L", "score_us": 0, "score_them": 49, "cap": -14},
            {"date": "2026-09-25", "opp": "Winchester", "loc": "Away", "result": "L", "score_us": 0, "score_them": 42, "cap": -14},
            {"date": "2026-10-02", "opp": "Arlington", "loc": "Away", "result": "L", "score_us": 0, "score_them": 35, "cap": -14},
            {"date": "2026-10-09", "opp": "Belmont", "loc": "Home", "result": "L", "score_us": 0, "score_them": 28, "cap": -14},
            {"date": "2026-10-16", "opp": "Melrose", "loc": "Away", "result": "L", "score_us": 0, "score_them": 35, "cap": -14},
            {"date": "2026-10-23", "opp": "Reading", "loc": "Away", "result": "L", "score_us": 0, "score_them": 62, "cap": -14},
            {"date": "2026-10-30", "opp": "Arlington", "loc": "Away", "result": "L (Forfeit)", "score_us": 0, "score_them": 2, "cap": -2}
        ]
    }
}

# --- Build Master Dataframe ---
rows = []
for team_name, data in teams_data.items():
    eligible = True if data["wins"] >= 3 else False
    rows.append({
        "School": team_name,
        "Record": data["record"],
        "Wins": data["wins"],
        "Margin": data["avg_margin"],
        "SoS": data["opp_rating"],
        "Rating": data["rating"],
        "Eligible": eligible
    })

df = pd.DataFrame(rows).sort_values(by="Rating", ascending=False).reset_index(drop=True)
qualified_df = df[df["Eligible"] == True].reset_index(drop=True)
qualified_df.insert(0, "#", range(1, len(qualified_df) + 1))

# --- CREATE TABS ---
tab_master, tab_bracket, tab_predictor = st.tabs([
    "📊 Master Standings & Bubble", 
    "🏆 Interactive Playoff Bracket", 
    "🔮 Math Score & Win Predictor"
])

# ==========================================
# TAB 1: MASTER STANDINGS & BUBBLE WATCH
# ==========================================
with tab_master:
    st.header("📊 Official MIAA Division 1 Standings (1–33)")
    st.caption("Includes official line numbers (#), victory margins (+/- 14 cap), and opponent ratings.")
    
    master_df = df.copy()
    master_df.insert(0, "#", range(1, len(master_df) + 1))
    st.dataframe(
        master_df[["#", "School", "Record", "Margin", "SoS", "Rating", "Eligible"]],
        column_config={
            "#": st.column_config.NumberColumn("Rank #", width="small"),
            "Margin": st.column_config.NumberColumn("Avg Margin", format="%+.4f"),
            "SoS": st.column_config.NumberColumn("Opponent Rating", format="%.4f"),
            "Rating": st.column_config.NumberColumn("Overall Rating", format="%.4f")
        },
        hide_index=True,
        use_container_width=True
    )
    
    st.divider()
    st.header("🫧 Playoff Bubble Watch")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Last Seeds In (#14–#16)")
        st.dataframe(
            qualified_df[["#", "School", "Record", "Rating"]].iloc[13:16],
            column_config={
                "#": st.column_config.NumberColumn("Seed #", width="small"),
                "Rating": st.column_config.NumberColumn("MIAA Rating", format="%.4f")
            },
            hide_index=True,
            use_container_width=True
        )
    with col2:
        st.subheader("Disqualified / Eliminated (Under 3 Wins)")
        elim_df = df[df["Eligible"] == False].reset_index(drop=True)
        elim_df.insert(0, "#", range(1, len(elim_df) + 1))
        st.dataframe(
            elim_df[["#", "School", "Record", "Wins", "Rating"]],
            column_config={
                "#": st.column_config.NumberColumn("Line #", width="small"),
                "Rating": st.column_config.NumberColumn("MIAA Rating", format="%.4f")
            },
            hide_index=True,
            use_container_width=True
        )

# ==========================================
# TAB 2: INTERACTIVE PLAYOFF BRACKET & TEAM INSPECTOR
# ==========================================
with tab_bracket:
    st.header("🏆 Interactive Division 1 Playoff Bracket")
    st.caption("Click or select any team from the 16-team tournament matchups to inspect their record, ratings, and dated schedule.")
    
    # 16-Team Bracket Matchups
    b_col1, b_col2 = st.columns(2)
    bracket_pairs = [
        (1, 16, "St. John's Prep", "Weymouth"),
        (2, 15, "Saint John's (Shrewsbury)", "Newton North"),
        (3, 14, "Central Catholic", "Everett"),
        (4, 13, "Springfield Central", "New Bedford"),
        (5, 12, "Wachusett Regional", "Haverhill"),
        (6, 11, "Xaverian Brothers", "Natick"),
        (7, 10, "Andover", "Brockton"),
        (8, 9, "Franklin", "Leominster"),
    ]
    
    with b_col1:
        st.subheader("Top Half Bracket")
        for s_high, s_low, t_high, t_low in bracket_pairs[:4]:
            st.info(f"**Matchup #{s_high} vs #{s_low}**: #{s_high} {t_high} vs. #{s_low} {t_low}")
            
    with b_col2:
        st.subheader("Bottom Half Bracket")
        for s_high, s_low, t_high, t_low in bracket_pairs[4:]:
            st.success(f"**Matchup #{s_high} vs #{s_low}**: #{s_high} {t_high} vs. #{s_low} {t_low}")

    st.divider()
    st.header("🔍 Interactive Team Inspector & Chronological Schedule")
    
    all_teams_sorted = sorted(list(teams_data.keys()))
    selected_team = st.selectbox("Click / Choose a Team to Inspect:", all_teams_sorted, index=all_teams_sorted.index("Newton North"))
    
    if selected_team:
        t_info = teams_data[selected_team]
        
        # Display Core Metrics
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("W-L Record", t_info["record"])
        c2.metric("Overall MIAA Rating", f"{t_info['rating']:.4f}")
        c3.metric("Avg Victory Margin", f"{t_info['avg_margin']:+.4f}")
        c4.metric("Opponent Rating (SoS)", f"{t_info['opp_rating']:.4f}")
        
        st.subheader(f"📅 Chronological Schedule & Scores: {selected_team}")
        st.write("Organized by date with **🟢 W** (Green Win) and **🔴 L** (Red Loss) indicators.")
        
        # Build Chronological Schedule Table
        sch_rows = []
        for g in sorted(t_info["schedule"], key=lambda x: x["date"]):
            res_badge = "🟢 W" if g["result"] == "W" else ("🔴 L" if g["result"] == "L" else "⏳ TBD")
            score_str = f"{g['score_us']} - {g['score_them']}" if g["score_us"] is not None else "Upcoming"
            cap_str = f"{g['cap']:+} pts" if g["score_us"] is not None else "-"
            
            sch_rows.append({
                "Date": g["date"],
                "Result": res_badge,
                "Opponent": g["opp"],
                "Location": g["loc"],
                "Final Score": score_str,
                "Capped Margin": cap_str
            })
        
        sch_df = pd.DataFrame(sch_rows)
        sch_df.index += 1
        st.dataframe(sch_df, hide_index=False, use_container_width=True)

# ==========================================
# TAB 3: MATH SCORE & WIN PREDICTOR
# ==========================================
with tab_predictor:
    st.header("🔮 Mathematical Matchup & Score Predictor")
    st.caption("Uses statistical probability (Logistic Rating Differential model & MIAA Margin Expectations) to predict outcomes.")
    
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        team_a_name = st.selectbox("Select Team A:", all_teams_sorted, index=all_teams_sorted.index("Newton North"))
    with p_col2:
        team_b_name = st.selectbox("Select Team B:", all_teams_sorted, index=all_teams_sorted.index("Saint John's (Shrewsbury)"))
        
    if team_a_name == team_b_name:
        st.warning("Please select two different teams for matchup prediction.")
    else:
        t_a = teams_data[team_a_name]
        t_b = teams_data[team_b_name]
        
        r_a = t_a["rating"]
        r_b = t_b["rating"]
        delta_r = r_a - r_b
        
        # Logistic Win Probability Model: P(A) = 1 / (1 + 10^(-delta_r / 10))
        prob_a = 1.0 / (1.0 + math.pow(10, -delta_r / 10.0))
        prob_b = 1.0 - prob_a
        
        # Projected Margin & Score Model
        # Base PPG ~ 27, baseline score calculation from margins and opponent ratings
        expected_margin = delta_r
        base_score_a = max(7, round(24 + (t_a["avg_margin"] / 2.0) + (delta_r / 3.0)))
        base_score_b = max(0, round(24 + (t_b["avg_margin"] / 2.0) - (delta_r / 3.0)))
        
        winner_name = team_a_name if prob_a >= 0.5 else team_b_name
        win_pct = max(prob_a, prob_b) * 100.0
        
        st.divider()
        st.subheader("🎯 Prediction Summary")
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Predicted Winner", winner_name, f"{win_pct:.1f}% Probability")
        m2.metric("Projected Score", f"{base_score_a} - {base_score_b}")
        m3.metric("Projected Point Spread", f"{team_a_name} by {abs(delta_r):.1f} pts" if delta_r > 0 else f"{team_b_name} by {abs(delta_r):.1f} pts")
        
        st.subheader("📊 Win Probability Distribution")
        prob_df = pd.DataFrame({
            "Team": [team_a_name, team_b_name],
            "Win Probability (%)": [prob_a * 100.0, prob_b * 100.0]
        })
        st.bar_chart(prob_df.set_index("Team"))
        
        st.subheader("🔬 Mathematical Rating Breakdown")
        comp_df = pd.DataFrame([
            {"Metric": "MIAA Overall Rating", team_a_name: f"{r_a:.4f}", team_b_name: f"{r_b:.4f}", "Advantage": team_a_name if r_a > r_b else team_b_name},
            {"Metric": "Avg Victory Margin (+/-14)", team_a_name: f"{t_a['avg_margin']:+.4f}", team_b_name: f"{t_b['avg_margin']:+.4f}", "Advantage": team_a_name if t_a['avg_margin'] > t_b['avg_margin'] else team_b_name},
            {"Metric": "Opponent Rating (SoS)", team_a_name: f"{t_a['opp_rating']:.4f}", team_b_name: f"{t_b['opp_rating']:.4f}", "Advantage": team_a_name if t_a['opp_rating'] > t_b['opp_rating'] else team_b_name},
        ])
        st.dataframe(comp_df, hide_index=True, use_container_width=True)
