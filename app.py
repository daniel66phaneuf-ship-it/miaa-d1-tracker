import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="MIAA D1 Football Leaderboard & Playoff Simulator",
    layout="wide",
    page_icon="🏈"
)

st.title("🏈 MIAA Division 1 Football Leaderboard & Playoff Simulator")
st.caption("Official MIAA Ratings & Standings (As of October 27) • Interactive Bracket, Matchup Predictor & Complete Schedules")

# --- 1. MASTER 33-TEAM DATABASE WITH PPG, PAPG, MASCOTS, COLORS & SCHEDULES ---
teams_data = {
    "St. John's Prep": {
        "record": "7-0", "wins": 7, "losses": 0, "rating": 27.7980, "avg_margin": 12.5714, "opp_rating": 15.2266,
        "ppg": 36.3, "papg": 17.7, "mascot": "Eagles", "color": "#00205B", "sec_color": "#A2AAAD",
        "next_game": "at Catholic Memorial (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Marshfield", "result": "W", "score": "35-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Londonderry (NH)", "result": "W", "score": "28-21", "margin": 7},
            {"date": "2026-09-25", "opponent": "Central Catholic", "result": "W", "score": "38-21", "margin": 14},
            {"date": "2026-10-02", "opponent": "La Salle Academy (RI)", "result": "W", "score": "42-14", "margin": 14},
            {"date": "2026-10-09", "opponent": "Malden Catholic", "result": "W", "score": "31-12", "margin": 14},
            {"date": "2026-10-16", "opponent": "Saint John's (Shrewsbury)", "result": "W", "score": "43-20", "margin": 14},
            {"date": "2026-10-23", "opponent": "Catholic Memorial", "result": "W", "score": "35-21", "margin": 14}
        ]
    },
    "Saint John's (Shrewsbury)": {
        "record": "6-1", "wins": 6, "losses": 1, "rating": 25.9005, "avg_margin": 10.0000, "opp_rating": 15.9005,
        "ppg": 31.4, "papg": 18.1, "mascot": "Pioneers", "color": "#C8102E", "sec_color": "#000000",
        "next_game": "at BC High (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Mansfield", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Doherty Memorial", "result": "W", "score": "35-7", "margin": 14},
            {"date": "2026-09-25", "opponent": "Shrewsbury", "result": "W", "score": "40-21", "margin": 14},
            {"date": "2026-10-02", "opponent": "Catholic Memorial", "result": "W", "score": "34-7", "margin": 14},
            {"date": "2026-10-09", "opponent": "Algonquin", "result": "W", "score": "27-18", "margin": 9},
            {"date": "2026-10-16", "opponent": "St. John's Prep", "result": "L", "score": "20-43", "margin": -14},
            {"date": "2026-10-23", "opponent": "Malden Catholic", "result": "W", "score": "36-17", "margin": 14}
        ]
    },
    "Central Catholic": {
        "record": "4-3", "wins": 4, "losses": 3, "rating": 23.6116, "avg_margin": 3.4286, "opp_rating": 20.1831,
        "ppg": 26.4, "papg": 21.7, "mascot": "Raiders", "color": "#C8102E", "sec_color": "#00205B",
        "next_game": "vs. Haverhill (10/29)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Springfield Central", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-18", "opponent": "St. John's Prep", "result": "L", "score": "21-38", "margin": -14},
            {"date": "2026-09-25", "opponent": "St. John's (Shrewsbury)", "result": "W", "score": "24-21", "margin": 3},
            {"date": "2026-10-02", "opponent": "Andover", "result": "W", "score": "42-24", "margin": 14},
            {"date": "2026-10-09", "opponent": "Londonderry (NH)", "result": "L", "score": "27-28", "margin": -1},
            {"date": "2026-10-16", "opponent": "Chelmsford", "result": "W", "score": "28-10", "margin": 14},
            {"date": "2026-10-23", "opponent": "Lowell", "result": "W", "score": "29-2", "margin": 14}
        ]
    },
    "Springfield Central": {
        "record": "6-1", "wins": 6, "losses": 1, "rating": 20.5456, "avg_margin": 9.0000, "opp_rating": 11.5456,
        "ppg": 38.5, "papg": 16.2, "mascot": "Golden Eagles", "color": "#FFC72C", "sec_color": "#000000",
        "next_game": "at West Springfield (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Central Catholic", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Iona Prep (NY)", "result": "L", "score": "21-35", "margin": -14},
            {"date": "2026-09-25", "opponent": "Minnechaug", "result": "W", "score": "42-7", "margin": 14},
            {"date": "2026-10-02", "opponent": "Westfield", "result": "W", "score": "45-12", "margin": 14},
            {"date": "2026-10-09", "opponent": "East Longmeadow", "result": "W", "score": "55-14", "margin": 14},
            {"date": "2026-10-16", "opponent": "West Springfield", "result": "W", "score": "42-14", "margin": 14},
            {"date": "2026-10-23", "opponent": "Holyoke", "result": "W", "score": "36-18", "margin": 14}
        ]
    },
    "Wachusett Regional": {
        "record": "7-0", "wins": 7, "losses": 0, "rating": 20.2372, "avg_margin": 11.0000, "opp_rating": 9.2372,
        "ppg": 35.0, "papg": 8.5, "mascot": "Mountaineers", "color": "#006A4E", "sec_color": "#FFFFFF",
        "next_game": "at Algonquin (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Fitchburg", "result": "W", "score": "35-0", "margin": 14},
            {"date": "2026-09-18", "opponent": "Shepherd Hill", "result": "W", "score": "28-7", "margin": 14},
            {"date": "2026-09-25", "opponent": "Nipmuc", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-02", "opponent": "Shrewsbury", "result": "W", "score": "38-14", "margin": 14},
            {"date": "2026-10-09", "opponent": "Grafton", "result": "W", "score": "38-0", "margin": 14},
            {"date": "2026-10-16", "opponent": "Westborough", "result": "W", "score": "42-0", "margin": 14},
            {"date": "2026-10-23", "opponent": "Leominster", "result": "W", "score": "43-24", "margin": 14}
        ]
    },
    "Xaverian Brothers": {
        "record": "3-4", "wins": 3, "losses": 4, "rating": 17.7758, "avg_margin": -0.2857, "opp_rating": 18.0616,
        "ppg": 22.1, "papg": 23.6, "mascot": "Hawks", "color": "#00205B", "sec_color": "#FFC72C",
        "next_game": "vs. Malden Catholic (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Everett", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Brockton", "result": "W", "score": "24-10", "margin": 14},
            {"date": "2026-09-25", "opponent": "St. John's Prep", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-02", "opponent": "Central Catholic", "result": "L", "score": "17-21", "margin": -4},
            {"date": "2026-10-09", "opponent": "BC High", "result": "W", "score": "47-6", "margin": 14},
            {"date": "2026-10-16", "opponent": "Catholic Memorial", "result": "L", "score": "21-42", "margin": -14},
            {"date": "2026-10-23", "opponent": "Saint John's (Shrewsbury)", "result": "L", "score": "10-24", "margin": -14}
        ]
    },
    "Andover": {
        "record": "5-2", "wins": 5, "losses": 2, "rating": 16.3508, "avg_margin": 3.7143, "opp_rating": 12.6365,
        "ppg": 28.3, "papg": 22.0, "mascot": "Golden Warriors", "color": "#00205B", "sec_color": "#FFC72C",
        "next_game": "at Tewksbury (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Billerica", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-09-18", "opponent": "Lowell", "result": "W", "score": "35-12", "margin": 14},
            {"date": "2026-09-25", "opponent": "Methuen", "result": "W", "score": "31-20", "margin": 11},
            {"date": "2026-10-02", "opponent": "Central Catholic", "result": "L", "score": "24-42", "margin": -14},
            {"date": "2026-10-09", "opponent": "North Andover", "result": "W", "score": "21-17", "margin": 4},
            {"date": "2026-10-16", "opponent": "Pinkerton (NH)", "result": "W", "score": "36-29", "margin": 7},
            {"date": "2026-10-23", "opponent": "Chelmsford", "result": "L", "score": "30-20", "margin": -10}
        ]
    },
    "Franklin": {
        "record": "5-2", "wins": 5, "losses": 2, "rating": 16.0439, "avg_margin": 5.4286, "opp_rating": 10.6153,
        "ppg": 24.1, "papg": 14.7, "mascot": "Panthers", "color": "#00205B", "sec_color": "#89CFF0",
        "next_game": "at Taunton (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Wachusett", "result": "L", "score": "14-21", "margin": -7},
            {"date": "2026-09-18", "opponent": "Milford", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-25", "opponent": "King Philip", "result": "L", "score": "10-21", "margin": -11},
            {"date": "2026-10-02", "opponent": "Milton", "result": "L", "score": "6-41", "margin": -14},
            {"date": "2026-10-09", "opponent": "Mansfield", "result": "W", "score": "35-0", "margin": 14},
            {"date": "2026-10-16", "opponent": "North Attleborough", "result": "W", "score": "28-0", "margin": 14},
            {"date": "2026-10-23", "opponent": "Attleboro", "result": "W", "score": "21-6", "margin": 14}
        ]
    },
    "Leominster": {
        "record": "4-3", "wins": 4, "losses": 3, "rating": 15.3921, "avg_margin": 3.2857, "opp_rating": 12.1064,
        "ppg": 25.0, "papg": 19.1, "mascot": "Blue Devils", "color": "#0033A0", "sec_color": "#000000",
        "next_game": "at Grafton (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Doherty Memorial", "result": "W", "score": "31-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Minnechaug", "result": "L", "score": "14-21", "margin": -7},
            {"date": "2026-09-25", "opponent": "Westborough", "result": "W", "score": "21-7", "margin": 14},
            {"date": "2026-10-02", "opponent": "Grafton", "result": "L", "score": "12-28", "margin": -14},
            {"date": "2026-10-09", "opponent": "Algonquin", "result": "W", "score": "35-14", "margin": 14},
            {"date": "2026-10-16", "opponent": "Shrewsbury", "result": "W", "score": "40-21", "margin": 14},
            {"date": "2026-10-23", "opponent": "Wachusett", "result": "L", "score": "24-43", "margin": -14}
        ]
    },
    "Brockton": {
        "record": "3-4", "wins": 3, "losses": 4, "rating": 10.8963, "avg_margin": -1.7143, "opp_rating": 12.6106,
        "ppg": 18.4, "papg": 21.3, "mascot": "Boxers", "color": "#800020", "sec_color": "#000000",
        "next_game": "at Durfee (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Xaverian", "result": "L", "score": "10-24", "margin": -14},
            {"date": "2026-09-18", "opponent": "Natick", "result": "L", "score": "14-21", "margin": -7},
            {"date": "2026-09-25", "opponent": "Bridgewater-Raynham", "result": "L", "score": "7-28", "margin": -14},
            {"date": "2026-10-02", "opponent": "New Bedford", "result": "L", "score": "14-20", "margin": -6},
            {"date": "2026-10-09", "opponent": "Durfee", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-16", "opponent": "Weymouth", "result": "W", "score": "21-8", "margin": 13},
            {"date": "2026-10-23", "opponent": "Taunton", "result": "W", "score": "35-24", "margin": 11}
        ]
    },
    "Natick": {
        "record": "4-3", "wins": 4, "losses": 3, "rating": 10.8125, "avg_margin": 2.1429, "opp_rating": 8.6697,
        "ppg": 23.7, "papg": 18.6, "mascot": "Redhawks", "color": "#C8102E", "sec_color": "#FFFFFF",
        "next_game": "at Walpole (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Needham", "result": "W", "score": "24-7", "margin": 14},
            {"date": "2026-09-18", "opponent": "Brockton", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-09-25", "opponent": "Walpole", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-02", "opponent": "Wellesley", "result": "W", "score": "37-14", "margin": 14},
            {"date": "2026-10-09", "opponent": "Brookline", "result": "W", "score": "27-6", "margin": 14},
            {"date": "2026-10-16", "opponent": "Newton North", "result": "W", "score": "37-14", "margin": 14},
            {"date": "2026-10-23", "opponent": "Milton", "result": "L", "score": "6-37", "margin": -14}
        ]
    },
    "Haverhill": {
        "record": "5-2", "wins": 5, "losses": 2, "rating": 10.6868, "avg_margin": 6.0000, "opp_rating": 4.6868,
        "ppg": 31.1, "papg": 22.4, "mascot": "Hillies", "color": "#4E3629", "sec_color": "#FFD700",
        "next_game": "at Central Catholic (10/29)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Lawrence", "result": "W", "score": "42-12", "margin": 14},
            {"date": "2026-09-18", "opponent": "Lowell", "result": "W", "score": "35-14", "margin": 14},
            {"date": "2026-09-25", "opponent": "Chelmsford", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-02", "opponent": "Methuen", "result": "W", "score": "40-34", "margin": 6},
            {"date": "2026-10-09", "opponent": "North Andover", "result": "W", "score": "28-21", "margin": 7},
            {"date": "2026-10-16", "opponent": "New Bedford", "result": "L", "score": "28-34", "margin": -6},
            {"date": "2026-10-23", "opponent": "Tewksbury", "result": "W", "score": "31-14", "margin": 14}
        ]
    },
    "New Bedford": {
        "record": "6-1", "wins": 6, "losses": 1, "rating": 10.4183, "avg_margin": 7.2857, "opp_rating": 3.1326,
        "ppg": 28.6, "papg": 18.1, "mascot": "Whalers", "color": "#C8102E", "sec_color": "#FFFFFF",
        "next_game": "at Dartmouth (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Durfee", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Barnstable", "result": "W", "score": "24-17", "margin": 7},
            {"date": "2026-09-25", "opponent": "Bridgewater-Raynham", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-02", "opponent": "Brockton", "result": "W", "score": "20-14", "margin": 6},
            {"date": "2026-10-09", "opponent": "Taunton", "result": "W", "score": "31-20", "margin": 11},
            {"date": "2026-10-16", "opponent": "Haverhill", "result": "W", "score": "34-28", "margin": 6},
            {"date": "2026-10-23", "opponent": "Dartmouth", "result": "W", "score": "28-14", "margin": 14}
        ]
    },
    "Everett": {
        "record": "6-1", "wins": 6, "losses": 1, "rating": 10.3895, "avg_margin": 5.7143, "opp_rating": 4.6752,
        "ppg": 27.3, "papg": 17.4, "mascot": "Crimson Tide", "color": "#9E1B32", "sec_color": "#FFD700",
        "next_game": "at Lynn Classical (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Xaverian", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-18", "opponent": "Somerville", "result": "W", "score": "27-26", "margin": 1},
            {"date": "2026-09-25", "opponent": "Lynn English", "result": "W", "score": "35-12", "margin": 14},
            {"date": "2026-10-02", "opponent": "Revere", "result": "W", "score": "28-7", "margin": 14},
            {"date": "2026-10-09", "opponent": "Medford", "result": "W", "score": "31-14", "margin": 14},
            {"date": "2026-10-16", "opponent": "Malden", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-23", "opponent": "Lynn Classical", "result": "W", "score": "28-21", "margin": 7}
        ]
    },
    "Methuen": {
        "record": "2-5", "wins": 2, "losses": 5, "rating": 8.8828, "avg_margin": -4.8571, "opp_rating": 13.7399,
        "ppg": 22.4, "papg": 29.1, "mascot": "Rangers", "color": "#00205B", "sec_color": "#FFFFFF",
        "next_game": "at Billerica (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Pinkerton (NH)", "result": "L", "score": "14-35", "margin": -14},
            {"date": "2026-09-18", "opponent": "North Andover", "result": "W", "score": "28-21", "margin": 7},
            {"date": "2026-09-25", "opponent": "Andover", "result": "L", "score": "20-31", "margin": -11},
            {"date": "2026-10-02", "opponent": "Haverhill", "result": "L", "score": "34-40", "margin": -6},
            {"date": "2026-10-09", "opponent": "Billerica", "result": "L", "score": "19-31", "margin": -12},
            {"date": "2026-10-16", "opponent": "Lawrence", "result": "W", "score": "42-12", "margin": 14},
            {"date": "2026-10-23", "opponent": "Central Catholic", "result": "L", "score": "0-34", "margin": -14}
        ]
    },
    "Shrewsbury": {
        "record": "3-4", "wins": 3, "losses": 4, "rating": 8.5019, "avg_margin": -4.4286, "opp_rating": 12.9305,
        "ppg": 20.1, "papg": 26.7, "mascot": "Colonials", "color": "#00205B", "sec_color": "#C5B358",
        "next_game": "at Westborough (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Grafton", "result": "W", "score": "24-14", "margin": 10},
            {"date": "2026-09-18", "opponent": "Acton-Boxborough", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-25", "opponent": "Saint John's (Shrewsbury)", "result": "L", "score": "21-40", "margin": -14},
            {"date": "2026-10-02", "opponent": "Wachusett", "result": "L", "score": "14-38", "margin": -14},
            {"date": "2026-10-09", "opponent": "Algonquin", "result": "W", "score": "27-18", "margin": 9},
            {"date": "2026-10-16", "opponent": "Leominster", "result": "L", "score": "21-40", "margin": -14},
            {"date": "2026-10-23", "opponent": "Westborough", "result": "L", "score": "6-23", "margin": -14}
        ]
    },
    "Boston College High": {
        "record": "1-6", "wins": 1, "losses": 6, "rating": 8.2511, "avg_margin": -8.7143, "opp_rating": 16.9654,
        "ppg": 14.2, "papg": 29.6, "mascot": "Eagles", "color": "#800020", "sec_color": "#FFD700",
        "next_game": "vs. Saint John's (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Catholic Memorial", "result": "L", "score": "7-35", "margin": -14},
            {"date": "2026-09-18", "opponent": "Central Catholic", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-25", "opponent": "Marshfield", "result": "L", "score": "10-24", "margin": -14},
            {"date": "2026-10-02", "opponent": "St. John's Prep", "result": "L", "score": "12-35", "margin": -14},
            {"date": "2026-10-09", "opponent": "Xaverian", "result": "L", "score": "6-47", "margin": -14},
            {"date": "2026-10-16", "opponent": "Malden Catholic", "result": "W", "score": "22-10", "margin": 12},
            {"date": "2026-10-23", "opponent": "Saint John's (Shrewsbury)", "result": "L", "score": "28-28", "margin": -7}
        ]
    },
    "Newton North": {
        "record": "6-1", "wins": 6, "losses": 1, "rating": 6.8728, "avg_margin": 6.7143, "opp_rating": 0.1585,
        "ppg": 23.4, "papg": 15.4, "mascot": "Tigers", "color": "#FF6600", "sec_color": "#000000",
        "next_game": "at Braintree (10/30)",
        "scores": [
            {"date": "2026-09-10", "opponent": "Waltham", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Newton South", "result": "W", "score": "20-14", "margin": 6},
            {"date": "2026-09-25", "opponent": "Weymouth", "result": "W", "score": "14-12", "margin": 2},
            {"date": "2026-10-02", "opponent": "Framingham", "result": "W", "score": "29-18", "margin": 11},
            {"date": "2026-10-09", "opponent": "Natick", "result": "L", "score": "14-37", "margin": -14},
            {"date": "2026-10-16", "opponent": "Wellesley", "result": "W", "score": "31-6", "margin": 14},
            {"date": "2026-10-23", "opponent": "Cumberland (R.I.)", "result": "W", "score": "26-7", "margin": 14}
        ]
    },
    "Weymouth": {
        "record": "5-2", "wins": 5, "losses": 2, "rating": 6.5816, "avg_margin": 4.5714, "opp_rating": 2.0102,
        "ppg": 21.3, "papg": 15.1, "mascot": "Wildcats", "color": "#800020", "sec_color": "#FFD700",
        "next_game": "vs. Milton (10/29)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Needham", "result": "W", "score": "33-15", "margin": 14},
            {"date": "2026-09-18", "opponent": "Braintree", "result": "W", "score": "28-7", "margin": 14},
            {"date": "2026-09-25", "opponent": "Newton North", "result": "L", "score": "12-14", "margin": -2},
            {"date": "2026-10-02", "opponent": "Framingham", "result": "W", "score": "24-10", "margin": 14},
            {"date": "2026-10-09", "opponent": "Milton", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-16", "opponent": "Brockton", "result": "L", "score": "8-21", "margin": -13},
            {"date": "2026-10-23", "opponent": "Wellesley", "result": "W", "score": "23-25", "margin": -2}
        ]
    },
    "Lowell": {
        "record": "2-5", "wins": 2, "losses": 5, "rating": 6.1900, "avg_margin": -4.2857, "opp_rating": 10.4757,
        "ppg": 18.3, "papg": 26.4, "mascot": "Red Raiders", "color": "#800020", "sec_color": "#FFFFFF",
        "next_game": "vs. North Andover (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Andover", "result": "L", "score": "12-35", "margin": -14},
            {"date": "2026-09-18", "opponent": "Haverhill", "result": "L", "score": "14-35", "margin": -14},
            {"date": "2026-09-25", "opponent": "Lawrence", "result": "W", "score": "46-0", "margin": 14},
            {"date": "2026-10-02", "opponent": "Billerica", "result": "L", "score": "18-41", "margin": -14},
            {"date": "2026-10-09", "opponent": "Chelmsford", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-16", "opponent": "Methuen", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-23", "opponent": "Central Catholic", "result": "L", "score": "3-29", "margin": -14}
        ]
    },
    "Framingham": {
        "record": "4-3", "wins": 4, "losses": 3, "rating": 4.3554, "avg_margin": 0.5714, "opp_rating": 3.7840,
        "ppg": 21.7, "papg": 20.6, "mascot": "Flyers", "color": "#00205B", "sec_color": "#FFFFFF",
        "next_game": "vs. Needham (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Brookline", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-09-18", "opponent": "Durfee", "result": "W", "score": "28-27", "margin": 1},
            {"date": "2026-09-25", "opponent": "Wellesley", "result": "W", "score": "24-14", "margin": 10},
            {"date": "2026-10-02", "opponent": "Newton North", "result": "L", "score": "18-29", "margin": -11},
            {"date": "2026-10-09", "opponent": "Weymouth", "result": "L", "score": "10-24", "margin": -14},
            {"date": "2026-10-16", "opponent": "Natick", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-23", "opponent": "Needham", "result": "W", "score": "37-8", "margin": 14}
        ]
    },
    "Taunton": {
        "record": "3-4", "wins": 3, "losses": 4, "rating": 4.0806, "avg_margin": -1.2857, "opp_rating": 5.3663,
        "ppg": 18.1, "papg": 20.4, "mascot": "Tigers", "color": "#FF6600", "sec_color": "#000000",
        "next_game": "vs. Franklin (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "New Bedford", "result": "L", "score": "20-31", "margin": -11},
            {"date": "2026-09-18", "opponent": "Attleboro", "result": "L", "score": "20-27", "margin": -7},
            {"date": "2026-09-25", "opponent": "Stoughton", "result": "W", "score": "21-8", "margin": 13},
            {"date": "2026-10-02", "opponent": "Milford", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-09", "opponent": "Franklin", "result": "L", "score": "12-28", "margin": -14},
            {"date": "2026-10-16", "opponent": "King Philip", "result": "W", "score": "18-14", "margin": 4},
            {"date": "2026-10-23", "opponent": "Brockton", "result": "W", "score": "22-7", "margin": 14}
        ]
    },
    "Durfee": {
        "record": "5-2", "wins": 5, "losses": 2, "rating": 3.9070, "avg_margin": 6.2857, "opp_rating": -2.3787,
        "ppg": 26.3, "papg": 16.0, "mascot": "Hilltoppers", "color": "#C8102E", "sec_color": "#000000",
        "next_game": "vs. Brockton (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "New Bedford", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-18", "opponent": "Framingham", "result": "L", "score": "27-28", "margin": -1},
            {"date": "2026-09-25", "opponent": "TechBoston", "result": "W", "score": "34-7", "margin": 14},
            {"date": "2026-10-02", "opponent": "Diman RVT", "result": "W", "score": "35-0", "margin": 14},
            {"date": "2026-10-09", "opponent": "Brockton", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-16", "opponent": "Dartmouth", "result": "W", "score": "28-21", "margin": 7},
            {"date": "2026-10-23", "opponent": "Somerset Berkley", "result": "W", "score": "25-7", "margin": 14}
        ]
    },
    "Attleboro": {
        "record": "3-4", "wins": 3, "losses": 4, "rating": 3.1732, "avg_margin": -3.2857, "opp_rating": 6.4589,
        "ppg": 17.4, "papg": 22.1, "mascot": "Blue Bombardiers", "color": "#00205B", "sec_color": "#C0C0C0",
        "next_game": "at Milford (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Mansfield", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-18", "opponent": "Taunton", "result": "W", "score": "27-20", "margin": 7},
            {"date": "2026-09-25", "opponent": "Milton", "result": "L", "score": "12-31", "margin": -14},
            {"date": "2026-10-02", "opponent": "Franklin", "result": "L", "score": "6-21", "margin": -14},
            {"date": "2026-10-09", "opponent": "King Philip", "result": "L", "score": "10-24", "margin": -14},
            {"date": "2026-10-16", "opponent": "North Attleborough", "result": "W", "score": "24-14", "margin": 10},
            {"date": "2026-10-23", "opponent": "Milford", "result": "W", "score": "28-17", "margin": 11}
        ]
    },
    "Acton-Boxborough": {
        "record": "3-3", "wins": 3, "losses": 3, "rating": 3.0709, "avg_margin": 0.5000, "opp_rating": 2.5709,
        "ppg": 24.5, "papg": 23.8, "mascot": "Revolution", "color": "#00205B", "sec_color": "#FFC72C",
        "next_game": "at Bedford (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Shrewsbury", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-18", "opponent": "Waltham", "result": "W", "score": "35-13", "margin": 14},
            {"date": "2026-09-25", "opponent": "Westford Academy", "result": "W", "score": "28-21", "margin": 7},
            {"date": "2026-10-02", "opponent": "Lincoln-Sudbury", "result": "L", "score": "10-24", "margin": -14},
            {"date": "2026-10-09", "opponent": "Wayland", "result": "L", "score": "30-47", "margin": -14},
            {"date": "2026-10-16", "opponent": "Concord-Carlisle", "result": "W", "score": "30-10", "margin": 14}
        ]
    },
    "Needham": {
        "record": "1-6", "wins": 1, "losses": 6, "rating": 2.7401, "avg_margin": -8.7143, "opp_rating": 11.4544,
        "ppg": 13.1, "papg": 28.0, "mascot": "Rockets", "color": "#00205B", "sec_color": "#FFC72C",
        "next_game": "at Framingham (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Natick", "result": "L", "score": "7-24", "margin": -14},
            {"date": "2026-09-18", "opponent": "Weymouth", "result": "L", "score": "15-33", "margin": -14},
            {"date": "2026-09-25", "opponent": "Milton", "result": "L", "score": "14-31", "margin": -14},
            {"date": "2026-10-02", "opponent": "Walpole", "result": "L", "score": "10-28", "margin": -14},
            {"date": "2026-10-09", "opponent": "Braintree", "result": "W", "score": "21-7", "margin": 14},
            {"date": "2026-10-16", "opponent": "Wellesley", "result": "L", "score": "17-28", "margin": -11},
            {"date": "2026-10-23", "opponent": "Framingham", "result": "L", "score": "8-37", "margin": -14}
        ]
    },
    "Arlington": {
        "record": "2-5", "wins": 2, "losses": 5, "rating": 0.1879, "avg_margin": -3.8571, "opp_rating": 4.0451,
        "ppg": 15.3, "papg": 22.6, "mascot": "Spy Ponders", "color": "#800020", "sec_color": "#FFFFFF",
        "next_game": "vs. Lexington (Forfeit W)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Reading", "result": "L", "score": "7-28", "margin": -14},
            {"date": "2026-09-18", "opponent": "Woburn", "result": "L", "score": "0-7", "margin": -7},
            {"date": "2026-09-25", "opponent": "Winchester", "result": "L", "score": "14-38", "margin": -14},
            {"date": "2026-10-02", "opponent": "Belmont", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-09", "opponent": "Melrose", "result": "L", "score": "14-24", "margin": -10},
            {"date": "2026-10-16", "opponent": "Wakefield", "result": "W", "score": "28-10", "margin": 14},
            {"date": "2026-10-23", "opponent": "Lexington", "result": "W", "score": "16-37", "margin": -14}
        ]
    },
    "Brookline": {
        "record": "3-4", "wins": 3, "losses": 4, "rating": -1.7666, "avg_margin": -3.5714, "opp_rating": 1.8049,
        "ppg": 16.2, "papg": 22.1, "mascot": "Warriors", "color": "#800020", "sec_color": "#00205B",
        "next_game": "at Wellesley (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Framingham", "result": "L", "score": "14-21", "margin": -7},
            {"date": "2026-09-18", "opponent": "Natick", "result": "L", "score": "6-27", "margin": -14},
            {"date": "2026-09-25", "opponent": "Newton South", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-02", "opponent": "Braintree", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-09", "opponent": "Walpole", "result": "L", "score": "7-35", "margin": -14},
            {"date": "2026-10-16", "opponent": "Cambridge", "result": "W", "score": "24-10", "margin": 14},
            {"date": "2026-10-23", "opponent": "Wellesley", "result": "L", "score": "13-34", "margin": -14}
        ]
    },
    "Lawrence": {
        "record": "1-6", "wins": 1, "losses": 6, "rating": -3.8168, "avg_margin": -10.2857, "opp_rating": 6.4689,
        "ppg": 10.4, "papg": 32.1, "mascot": "Lancers", "color": "#00205B", "sec_color": "#FFFFFF",
        "next_game": "vs. Chelmsford (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Haverhill", "result": "L", "score": "12-42", "margin": -14},
            {"date": "2026-09-18", "opponent": "Chelmsford", "result": "L", "score": "7-35", "margin": -14},
            {"date": "2026-09-25", "opponent": "Lowell", "result": "L", "score": "0-46", "margin": -14},
            {"date": "2026-10-02", "opponent": "North Andover", "result": "L", "score": "14-38", "margin": -14},
            {"date": "2026-10-09", "opponent": "Methuen", "result": "L", "score": "12-42", "margin": -14},
            {"date": "2026-10-16", "opponent": "Lynn English", "result": "W", "score": "21-7", "margin": 14},
            {"date": "2026-10-23", "opponent": "Billerica", "result": "L", "score": "7-35", "margin": -14}
        ]
    },
    "Braintree": {
        "record": "1-6", "wins": 1, "losses": 6, "rating": -5.6503, "avg_margin": -10.8571, "opp_rating": 5.2069,
        "ppg": 10.1, "papg": 31.4, "mascot": "Wamps", "color": "#0000FF", "sec_color": "#FFFFFF",
        "next_game": "vs. Newton North (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Walpole", "result": "L", "score": "7-48", "margin": -14},
            {"date": "2026-09-18", "opponent": "Weymouth", "result": "L", "score": "7-28", "margin": -14},
            {"date": "2026-09-25", "opponent": "Wellesley", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-02", "opponent": "Brookline", "result": "L", "score": "14-21", "margin": -7},
            {"date": "2026-10-09", "opponent": "Needham", "result": "L", "score": "7-21", "margin": -14},
            {"date": "2026-10-16", "opponent": "Milton", "result": "L", "score": "0-35", "margin": -14},
            {"date": "2026-10-23", "opponent": "Quincy", "result": "W", "score": "21-14", "margin": 7}
        ]
    },
    "Newton South": {
        "record": "1-6", "wins": 1, "losses": 6, "rating": -6.9349, "avg_margin": -7.0000, "opp_rating": 0.0651,
        "ppg": 15.2, "papg": 26.4, "mascot": "Lions", "color": "#FF6600", "sec_color": "#0000FF",
        "next_game": "at Westford (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Waltham", "result": "L", "score": "12-28", "margin": -14},
            {"date": "2026-09-18", "opponent": "Newton North", "result": "L", "score": "14-20", "margin": -6},
            {"date": "2026-09-25", "opponent": "Brookline", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-02", "opponent": "Cambridge", "result": "L", "score": "20-21", "margin": -1},
            {"date": "2026-10-09", "opponent": "Weston", "result": "L", "score": "14-35", "margin": -14},
            {"date": "2026-10-16", "opponent": "Boston Latin", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-23", "opponent": "Wayland", "result": "L", "score": "12-38", "margin": -14}
        ]
    },
    "Belmont": {
        "record": "2-5", "wins": 2, "losses": 5, "rating": -10.3076, "avg_margin": -7.1429, "opp_rating": -3.1647,
        "ppg": 11.0, "papg": 28.3, "mascot": "Marauders", "color": "#00205B", "sec_color": "#800020",
        "next_game": "vs. Winchester (10/30)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Woburn", "result": "L", "score": "0-49", "margin": -14},
            {"date": "2026-09-18", "opponent": "Reading", "result": "L", "score": "0-41", "margin": -14},
            {"date": "2026-09-25", "opponent": "Lexington", "result": "W", "score": "35-14", "margin": 14},
            {"date": "2026-10-02", "opponent": "Arlington", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-09", "opponent": "Melrose", "result": "L", "score": "7-35", "margin": -14},
            {"date": "2026-10-16", "opponent": "Wakefield", "result": "L", "score": "7-28", "margin": -14},
            {"date": "2026-10-23", "opponent": "Watertown", "result": "W", "score": "14-7", "margin": 7}
        ]
    },
    "Lexington": {
        "record": "0-7", "wins": 0, "losses": 7, "rating": -13.5601, "avg_margin": -14.0000, "opp_rating": 0.4399,
        "ppg": 4.1, "papg": 38.0, "mascot": "Minutemen", "color": "#0000FF", "sec_color": "#FFD700",
        "next_game": "at Arlington (Forfeit L)",
        "scores": [
            {"date": "2026-09-11", "opponent": "Reading", "result": "L", "score": "0-62", "margin": -14},
            {"date": "2026-09-18", "opponent": "Melrose", "result": "L", "score": "7-42", "margin": -14},
            {"date": "2026-09-25", "opponent": "Belmont", "result": "L", "score": "14-35", "margin": -14},
            {"date": "2026-10-02", "opponent": "Woburn", "result": "L", "score": "0-42", "margin": -14},
            {"date": "2026-10-09", "opponent": "Winchester", "result": "L", "score": "8-40", "margin": -14},
            {"date": "2026-10-16", "opponent": "Wilmington", "result": "L", "score": "0-28", "margin": -14},
            {"date": "2026-10-23", "opponent": "Arlington", "result": "L", "score": "0-17", "margin": -14}
        ]
    }
}

# --- 2. ADVANCED MATHEMATICAL PREDICTION MODEL (PPG, PAPG, SOS & MIAA RATING) ---
def predict_matchup(team_a_name, team_b_name):
    ta = teams_data[team_a_name]
    tb = teams_data[team_b_name]

    # Formula incorporating actual points scored (PPG), points allowed (PAPG), Strength of Schedule (SoS) and MIAA Rating
    exp_score_a = max(3.0, (ta['ppg'] + tb['papg']) / 2.0 + 0.35 * (ta['opp_rating'] - tb['opp_rating']))
    exp_score_b = max(3.0, (tb['ppg'] + ta['papg']) / 2.0 + 0.35 * (tb['opp_rating'] - ta['opp_rating']))

    # MIAA Rating Differential Adjuster
    rating_diff = ta['rating'] - tb['rating']
    score_diff = exp_score_a - exp_score_b
    combined_diff = 0.5 * rating_diff + 0.5 * score_diff

    # Logistic Win Probability Curve
    win_prob_a = 1.0 / (1.0 + 10.0 ** (-combined_diff / 12.0))
    win_prob_b = 1.0 - win_prob_a

    # Integer rounded score
    final_score_a = int(round(exp_score_a))
    final_score_b = int(round(exp_score_b))

    if final_score_a == final_score_b:
        if win_prob_a >= 0.5:
            final_score_a += 3
        else:
            final_score_b += 3

    if win_prob_a >= 0.5:
        winner = team_a_name
        winner_prob = win_prob_a * 100.0
    else:
        winner = team_b_name
        winner_prob = win_prob_b * 100.0

    return {
        "winner": winner,
        "winner_prob": winner_prob,
        "score_a": final_score_a,
        "score_b": final_score_b,
        "prob_a": win_prob_a * 100.0,
        "prob_b": win_prob_b * 100.0
    }

# Build Qualified Leaderboard DataFrame
df_rows = []
for school, d in teams_data.items():
    # MIAA 3-Win Postseason Eligibility Rule
    eligible = True if d["wins"] >= 3 else False
    df_rows.append({
        "School": school,
        "Mascot": d["mascot"],
        "Record": d["record"],
        "Wins": d["wins"],
        "PPG": d["ppg"],
        "PAPG": d["papg"],
        "Margin": d["avg_margin"],
        "SoS": d["opp_rating"],
        "Rating": d["rating"],
        "Eligible": eligible,
        "Next Game": d["next_game"]
    })

full_df = pd.DataFrame(df_rows).sort_values(by="Rating", ascending=False).reset_index(drop=True)
qualified_df = full_df[full_df["Eligible"] == True].reset_index(drop=True)
qualified_df.insert(0, "#", range(1, len(qualified_df) + 1))

# --- 3. NAVIGATION TABS ---
tab_bracket, tab_predictor, tab_inspector, tab_leaderboard = st.tabs([
    "🏆 Playoff Bracket & Winner Predictions",
    "🔮 Advanced Matchup Predictor",
    "🔍 Team Inspector & Schedules",
    "📊 Master Division 1 Leaderboard"
])

# --- TAB 1: PLAYOFF BRACKET & WINNER PREDICTIONS ---
with tab_bracket:
    st.header("🏆 Official Division 1 Playoff Bracket & First Round Predictions")
    st.caption("Active 16-Team Bracket applying MIAA 3-win minimum rule [SOURCE_CONTENT_TYPE_URL]. Each matchup features calculated winner predictions using real PPG, PAPG, and MIAA Rating data.")

    # Top 16 Seeds
    bracket_teams = qualified_df.head(16)["School"].tolist()

    # Standard 16-team tournament seeding pairings
    pairings = [
        (1, 16), (8, 9),
        (5, 12), (4, 13),
        (3, 14), (6, 11),
        (7, 10), (2, 15)
    ]

    st.subheader("Round 1 Postseason Matchups & Predicted Outcomes")

    for seed_a, seed_b in pairings:
        team_a = bracket_teams[seed_a - 1]
        team_b = bracket_teams[seed_b - 1]

        ta = teams_data[team_a]
        tb = teams_data[team_b]

        pred = predict_matchup(team_a, team_b)

        with st.container(border=True):
            col1, col2, col3 = st.columns([2, 1, 2])

            with col1:
                st.markdown(f"### **#{seed_a} {team_a}**")
                st.caption(f"**{ta['mascot']}** • Record: {ta['record']} • Rating: **{ta['rating']:.4f}**")
                st.write(f"📊 Offense: **{ta['ppg']} PPG** | Defense: **{ta['papg']} PAPG**")

            with col2:
                st.markdown("<h3 style='text-align: center; color: #3B82F6;'>VS</h3>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align: center; font-weight: bold; font-size: 1.1em;'>Predicted Final:<br><b>{pred['score_a']} - {pred['score_b']}</b></p>", unsafe_allow_html=True)

            with col3:
                st.markdown(f"### **#{seed_b} {team_b}**")
                st.caption(f"**{tb['mascot']}** • Record: {tb['record']} • Rating: **{tb['rating']:.4f}**")
                st.write(f"📊 Offense: **{tb['ppg']} PPG** | Defense: **{tb['papg']} PAPG**")

            # Prediction Highlight Banner
            st.info(f"🏆 **PREDICTED WINNER**: **{pred['winner']}** ({pred['winner_prob']:.1f}% Win Probability)")

# --- TAB 2: ADVANCED MATCHUP PREDICTOR ---
with tab_predictor:
    st.header("🔮 Custom Head-to-Head Matchup Predictor")
    st.caption("Simulate any matchup across all 33 MIAA Division 1 teams using actual PPG, PAPG, Opponent Rating (SoS), and Victory Margins.")

    c1, c2 = st.columns(2)
    with c1:
        team_a_sel = st.selectbox("Select Team A:", sorted(list(teams_data.keys())), index=sorted(list(teams_data.keys())).index("Newton North"))
    with c2:
        team_b_sel = st.selectbox("Select Team B:", sorted(list(teams_data.keys())), index=sorted(list(teams_data.keys())).index("Saint John's (Shrewsbury)"))

    if team_a_sel == team_b_sel:
        st.warning("Please select two different teams to simulate a matchup.")
    else:
        res = predict_matchup(team_a_sel, team_b_sel)
        ta = teams_data[team_a_sel]
        tb = teams_data[team_b_sel]

        st.subheader(f"Simulation Result: {team_a_sel} vs. {team_b_sel}")

        m1, m2, m3 = st.columns(3)
        m1.metric(f"Predicted Winner", f"🏆 {res['winner']}", f"{res['winner_prob']:.1f}% Confidence")
        m2.metric(f"Predicted Final Score", f"{res['score_a']} - {res['score_b']}")
        m3.metric(f"Point Spread", f"{res['winner']} by {abs(res['score_a'] - res['score_b'])} pts")

        st.divider()

        # Detailed Stats Comparison Table
        st.subheader("📊 Tail-of-the-Tape Statistical Comparison")
        comp_data = {
            "Metric": ["W-L Record", "MIAA Power Rating", "Avg. Points Scored (PPG)", "Avg. Points Allowed (PAPG)", "Avg. Capped Margin", "Opponent Rating (SoS)"],
            team_a_sel: [ta["record"], f"{ta['rating']:.4f}", f"{ta['ppg']} pts", f"{ta['papg']} pts", f"{ta['avg_margin']:+.4f}", f"{ta['opp_rating']:.4f}"],
            team_b_sel: [tb["record"], f"{tb['rating']:.4f}", f"{tb['ppg']} pts", f"{tb['papg']} pts", f"{tb['avg_margin']:+.4f}", f"{tb['opp_rating']:.4f}"]
        }
        st.dataframe(pd.DataFrame(comp_data), hide_index=True, use_container_width=True)

# --- TAB 3: TEAM INSPECTOR & SCHEDULES ---
with tab_inspector:
    st.header("🔍 Team Inspector & Chronological Game Schedules")
    insp_team = st.selectbox("Choose a School to Inspect:", sorted(list(teams_data.keys())), key="inspector_select")

    if insp_team:
        t = teams_data[insp_team]
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("W-L Record", t["record"])
        col2.metric("MIAA Rating", f"{t['rating']:.4f}")
        col3.metric("Avg Scored (PPG)", f"{t['ppg']} pts")
        col4.metric("Avg Allowed (PAPG)", f"{t['papg']} pts")
        col5.metric("Week 8 Game", t["next_game"])

        st.subheader(f"📅 2026 Game Schedule & Score Log for {insp_team} ({t['mascot']})")

        sch_rows = []
        for g in t["scores"]:
            status_badge = "🟢 W" if g["result"] == "W" else "🔴 L"
            sch_rows.append({
                "Date": g["date"],
                "Outcome": status_badge,
                "Opponent": g["opponent"],
                "Final Score": g["score"],
                "Capped Margin": f"{g['margin']:+d} pts"
            })

        sch_df = pd.DataFrame(sch_rows)
        st.dataframe(sch_df, hide_index=True, use_container_width=True)

# --- TAB 4: MASTER LEADERBOARD (FULL PAGE VIEW) ---
with tab_leaderboard:
    st.header("📊 Full MIAA Division 1 Master Leaderboard (All 33 Schools)")
    st.caption("Displayed in full page height format with explicit rank line numbers (#) on the side.")

    master_df = full_df.copy()
    master_df.insert(0, "#", range(1, len(master_df) + 1))

    # Height set to 1250px so all 33 rows render full-page without internal widget scrollbar
    st.dataframe(
        master_df[["#", "School", "Mascot", "Record", "PPG", "PAPG", "Margin", "SoS", "Rating", "Eligible"]],
        column_config={
            "#": st.column_config.NumberColumn("Rank #", width="small"),
            "PPG": st.column_config.NumberColumn("Avg Scored (PPG)", format="%.1f pts"),
            "PAPG": st.column_config.NumberColumn("Avg Allowed (PAPG)", format="%.1f pts"),
            "Margin": st.column_config.NumberColumn("Avg Margin (+/-14)", format="%+.4f"),
            "SoS": st.column_config.NumberColumn("Opponent Rating", format="%.4f"),
            "Rating": st.column_config.NumberColumn("Overall Rating", format="%.4f"),
            "Eligible": st.column_config.CheckboxColumn("3-Win Eligible")
        },
        hide_index=True,
        height=1250,
        use_container_width=True
    )
