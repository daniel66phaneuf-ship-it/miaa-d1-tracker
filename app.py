import pandas as pd
import streamlit as st
import numpy as np

# Page configuration
st.set_page_config(page_title="MIAA D1 Football Playoff Tracker & Bracket", layout="wide", page_icon="🏈")

# --- CUSTOM CSS FOR BRACKET & TEAM CARDS ---
st.markdown("""
<style>
    .bracket-container {
        display: flex;
        flex-direction: column;
        gap: 15px;
        margin-top: 10px;
    }
    .matchup-card {
        background-color: #1E293B;
        border-radius: 10px;
        padding: 12px 18px;
        border-left: 6px solid #3B82F6;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        margin-bottom: 12px;
    }
    .team-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 6px 0;
    }
    .team-badge {
        font-weight: bold;
        font-size: 1.05rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .color-pill {
        display: inline-block;
        width: 14px;
        height: 14px;
        border-radius: 50%;
        border: 1px solid #FFF;
    }
    .mascot-tag {
        font-size: 0.85rem;
        color: #94A3B8;
        font-weight: normal;
        margin-left: 4px;
    }
    .seed-tag {
        background-color: #334155;
        color: #F8FAFC;
        padding: 2px 8px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: bold;
    }
    .rating-val {
        font-family: monospace;
        font-size: 0.95rem;
        color: #38BDF8;
    }
</style>
""", unsafe_allow_html=True)

# --- 1. FULL 33-TEAM DATABASE WITH MASCOTS & COLORS ---
teams_data = {
    "St. John's Prep": {
        "mascot": "Eagles", "colors": ["#0A192F", "#FFFFFF", "#808080"], "color_text": "Navy, White, Gray",
        "record": "7-0", "wins": 7, "losses": 0, "rating": 27.7980, "avg_margin": 12.5714, "opp_rating": 15.2266,
        "scores": [
            {"date": "2026-09-11", "opponent": "Londonderry (NH)", "result": "W", "score": "35-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Central Catholic", "result": "W", "score": "42-21", "margin": 14},
            {"date": "2026-09-25", "opponent": "Haverhill", "result": "W", "score": "41-7", "margin": 14},
            {"date": "2026-10-02", "opponent": "Malden Catholic", "result": "W", "score": "31-12", "margin": 14},
            {"date": "2026-10-09", "opponent": "Saint John's (Shrewsbury)", "result": "W", "score": "43-20", "margin": 14},
            {"date": "2026-10-16", "opponent": "Catholic Memorial", "result": "W", "score": "35-21", "margin": 14},
            {"date": "2026-10-23", "opponent": "Xaverian Brothers", "result": "W", "score": "28-14", "margin": 14}
        ],
        "next_game": "at Catholic Memorial (10/30)"
    },
    "Saint John's (Shrewsbury)": {
        "mascot": "Pioneers", "colors": ["#CC0000", "#FFFFFF", "#000000"], "color_text": "Red, White, Black",
        "record": "6-1", "wins": 6, "losses": 1, "rating": 25.9005, "avg_margin": 10.0000, "opp_rating": 15.9005,
        "scores": [
            {"date": "2026-09-11", "opponent": "Mansfield", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Doherty", "result": "W", "score": "35-7", "margin": 14},
            {"date": "2026-09-25", "opponent": "Catholic Memorial", "result": "W", "score": "34-7", "margin": 14},
            {"date": "2026-10-02", "opponent": "Algonquin", "result": "W", "score": "27-18", "margin": 9},
            {"date": "2026-10-09", "opponent": "St. John's Prep", "result": "L", "score": "20-43", "margin": -14},
            {"date": "2026-10-16", "opponent": "Malden Catholic", "result": "W", "score": "42-10", "margin": 14},
            {"date": "2026-10-23", "opponent": "Xaverian", "result": "W", "score": "28-14", "margin": 14}
        ],
        "next_game": "at BC High (10/30)"
    },
    "Central Catholic": {
        "mascot": "Raiders", "colors": ["#CC0000", "#003399", "#FFFFFF"], "color_text": "Red, Blue, White",
        "record": "4-3", "wins": 4, "losses": 3, "rating": 23.6116, "avg_margin": 3.4286, "opp_rating": 20.1831,
        "scores": [
            {"date": "2026-09-11", "opponent": "Springfield Central", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-18", "opponent": "St. John's Prep", "result": "L", "score": "21-42", "margin": -14},
            {"date": "2026-09-25", "opponent": "St. John's (Shrewsbury)", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-02", "opponent": "Andover", "result": "W", "score": "42-24", "margin": 14},
            {"date": "2026-10-09", "opponent": "Lowell", "result": "W", "score": "35-7", "margin": 14},
            {"date": "2026-10-16", "opponent": "Chelmsford", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-23", "opponent": "Methuen", "result": "W", "score": "31-10", "margin": 14}
        ],
        "next_game": "vs. Haverhill (10/29)"
    },
    "Springfield Central": {
        "mascot": "Golden Eagles", "colors": ["#FFCC00", "#000000", "#FFFFFF"], "color_text": "Yellow, Black, White",
        "record": "6-1", "wins": 6, "losses": 1, "rating": 20.5456, "avg_margin": 9.0000, "opp_rating": 11.5456,
        "scores": [
            {"date": "2026-09-11", "opponent": "Central Catholic", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Iona Prep (NY)", "result": "L", "score": "20-35", "margin": -14},
            {"date": "2026-09-25", "opponent": "Minnechaug", "result": "W", "score": "42-7", "margin": 14},
            {"date": "2026-10-02", "opponent": "West Springfield", "result": "W", "score": "42-14", "margin": 14},
            {"date": "2026-10-09", "opponent": "East Longmeadow", "result": "W", "score": "55-14", "margin": 14},
            {"date": "2026-10-16", "opponent": "Longmeadow", "result": "W", "score": "35-7", "margin": 14},
            {"date": "2026-10-23", "opponent": "Chicopee Comp", "result": "W", "score": "49-0", "margin": 14}
        ],
        "next_game": "at West Springfield (10/30)"
    },
    "Wachusett Regional": {
        "mascot": "Mountaineers", "colors": ["#006633", "#FFFFFF", "#003300"], "color_text": "Green, White",
        "record": "7-0", "wins": 7, "losses": 0, "rating": 20.2372, "avg_margin": 11.0000, "opp_rating": 9.2372,
        "scores": [
            {"date": "2026-09-11", "opponent": "Fitchburg", "result": "W", "score": "35-0", "margin": 14},
            {"date": "2026-09-18", "opponent": "Marlborough", "result": "W", "score": "28-7", "margin": 14},
            {"date": "2026-09-25", "opponent": "Shepherd Hill", "result": "W", "score": "42-6", "margin": 14},
            {"date": "2026-10-02", "opponent": "Shrewsbury", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-09", "opponent": "Leominster", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-16", "opponent": "Grafton", "result": "W", "score": "38-0", "margin": 14},
            {"date": "2026-10-23", "opponent": "Westborough", "result": "W", "score": "42-0", "margin": 14}
        ],
        "next_game": "at Algonquin (10/30)"
    },
    "Xaverian Brothers": {
        "mascot": "Hawks", "colors": ["#FFCC00", "#0A192F", "#FFFFFF"], "color_text": "Yellow, Navy Blue",
        "record": "3-4", "wins": 3, "losses": 4, "rating": 17.7758, "avg_margin": -0.2857, "opp_rating": 18.0616,
        "scores": [
            {"date": "2026-09-11", "opponent": "Everett", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Brockton", "result": "W", "score": "24-10", "margin": 14},
            {"date": "2026-09-25", "opponent": "Catholic Memorial", "result": "L", "score": "21-42", "margin": -14},
            {"date": "2026-10-02", "opponent": "St. John's Prep", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-09", "opponent": "Saint John's (Shrewsbury)", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-16", "opponent": "BC High", "result": "W", "score": "47-6", "margin": 14},
            {"date": "2026-10-23", "opponent": "Malden Catholic", "result": "L", "score": "14-21", "margin": -7}
        ],
        "next_game": "vs. Malden Catholic (10/30)"
    },
    "Andover": {
        "mascot": "Golden Warriors", "colors": ["#0A192F", "#FFD700", "#FFFFFF"], "color_text": "Navy Blue, White",
        "record": "5-2", "wins": 5, "losses": 2, "rating": 16.3508, "avg_margin": 3.7143, "opp_rating": 12.6365,
        "scores": [
            {"date": "2026-09-11", "opponent": "Billerica", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Lawrence", "result": "W", "score": "42-0", "margin": 14},
            {"date": "2026-09-25", "opponent": "Methuen", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-02", "opponent": "Central Catholic", "result": "L", "score": "24-42", "margin": -14},
            {"date": "2026-10-09", "opponent": "Lowell", "result": "W", "score": "35-14", "margin": 14},
            {"date": "2026-10-16", "opponent": "Pinkerton (NH)", "result": "W", "score": "36-29", "margin": 7},
            {"date": "2026-10-23", "opponent": "Chelmsford", "result": "L", "score": "14-28", "margin": -14}
        ],
        "next_game": "at Tewksbury (10/30)"
    },
    "Franklin": {
        "mascot": "Panthers", "colors": ["#0A192F", "#89CFF0", "#FFFFFF"], "color_text": "Navy Blue, Baby Blue",
        "record": "5-2", "wins": 5, "losses": 2, "rating": 16.0439, "avg_margin": 5.4286, "opp_rating": 10.6153,
        "scores": [
            {"date": "2026-09-11", "opponent": "Wachusett", "result": "L", "score": "14-21", "margin": -7},
            {"date": "2026-09-18", "opponent": "Milford", "result": "L", "score": "6-41", "margin": -14},
            {"date": "2026-09-25", "opponent": "King Philip", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-02", "opponent": "Mansfield", "result": "W", "score": "28-7", "margin": 14},
            {"date": "2026-10-09", "opponent": "Attleboro", "result": "W", "score": "21-6", "margin": 14},
            {"date": "2026-10-16", "opponent": "Oliver Ames", "result": "W", "score": "35-0", "margin": 14},
            {"date": "2026-10-23", "opponent": "Taunton", "result": "W", "score": "28-10", "margin": 14}
        ],
        "next_game": "at Taunton (10/30)"
    },
    "Leominster": {
        "mascot": "Blue Devils", "colors": ["#0033CC", "#FFFFFF", "#000000"], "color_text": "Blue, White, Black",
        "record": "4-3", "wins": 4, "losses": 3, "rating": 15.3921, "avg_margin": 3.2857, "opp_rating": 12.1064,
        "scores": [
            {"date": "2026-09-11", "opponent": "Doherty", "result": "W", "score": "35-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Grafton", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-25", "opponent": "Westborough", "result": "W", "score": "21-7", "margin": 14},
            {"date": "2026-10-02", "opponent": "Algonquin", "result": "L", "score": "14-21", "margin": -7},
            {"date": "2026-10-09", "opponent": "Wachusett", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-16", "opponent": "Shrewsbury", "result": "W", "score": "40-21", "margin": 14},
            {"date": "2026-10-23", "opponent": "Shepherd Hill", "result": "L", "score": "14-28", "margin": -14}
        ],
        "next_game": "at Grafton (10/30)"
    },
    "Brockton": {
        "mascot": "Boxers", "colors": ["#800000", "#000000", "#FFFFFF"], "color_text": "Maroon, Black, White",
        "record": "3-4", "wins": 3, "losses": 4, "rating": 10.8963, "avg_margin": -1.7143, "opp_rating": 12.6106,
        "scores": [
            {"date": "2026-09-11", "opponent": "Xaverian", "result": "L", "score": "10-24", "margin": -14},
            {"date": "2026-09-18", "opponent": "BC High", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-25", "opponent": "New Bedford", "result": "L", "score": "14-20", "margin": -6},
            {"date": "2026-10-02", "opponent": "Weymouth", "result": "W", "score": "21-8", "margin": 13},
            {"date": "2026-10-09", "opponent": "Durfee", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-16", "opponent": "Bridgewater-Raynham", "result": "L", "score": "12-28", "margin": -14},
            {"date": "2026-10-23", "opponent": "Barnstable", "result": "W", "score": "20-14", "margin": 6}
        ],
        "next_game": "at Durfee (10/30)"
    },
    "Natick": {
        "mascot": "Redhawks", "colors": ["#CC0000", "#FFFFFF"], "color_text": "Red, White",
        "record": "4-3", "wins": 4, "losses": 3, "rating": 10.8125, "avg_margin": 2.1429, "opp_rating": 8.6697,
        "scores": [
            {"date": "2026-09-11", "opponent": "Needham", "result": "W", "score": "28-7", "margin": 14},
            {"date": "2026-09-18", "opponent": "Walpole", "result": "L", "score": "14-21", "margin": -7},
            {"date": "2026-09-25", "opponent": "Wellesley", "result": "W", "score": "37-14", "margin": 14},
            {"date": "2026-10-02", "opponent": "Brookline", "result": "W", "score": "27-6", "margin": 14},
            {"date": "2026-10-09", "opponent": "Newton North", "result": "W", "score": "37-14", "margin": 14},
            {"date": "2026-10-16", "opponent": "Milton", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-23", "opponent": "Framingham", "result": "L", "score": "10-28", "margin": -18}
        ],
        "next_game": "at Walpole (10/30)"
    },
    "Haverhill": {
        "mascot": "Hillies", "colors": ["#5C4033", "#FFD700"], "color_text": "Brown, Gold",
        "record": "5-2", "wins": 5, "losses": 2, "rating": 10.6868, "avg_margin": 6.0000, "opp_rating": 4.6868,
        "scores": [
            {"date": "2026-09-11", "opponent": "Lowell", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Chelmsford", "result": "W", "score": "21-7", "margin": 14},
            {"date": "2026-09-25", "opponent": "Methuen", "result": "W", "score": "40-34", "margin": 6},
            {"date": "2026-10-02", "opponent": "New Bedford", "result": "L", "score": "28-34", "margin": -6},
            {"date": "2026-10-09", "opponent": "Lawrence", "result": "W", "score": "35-0", "margin": 14},
            {"date": "2026-10-16", "opponent": "North Andover", "result": "W", "score": "24-10", "margin": 14},
            {"date": "2026-10-23", "opponent": "Tewksbury", "result": "L", "score": "14-28", "margin": -14}
        ],
        "next_game": "at Central Catholic (10/29)"
    },
    "New Bedford": {
        "mascot": "Whalers", "colors": ["#CC0000", "#FFFFFF"], "color_text": "Red, White",
        "record": "6-1", "wins": 6, "losses": 1, "rating": 10.4183, "avg_margin": 7.2857, "opp_rating": 3.1326,
        "scores": [
            {"date": "2026-09-11", "opponent": "Durfee", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Taunton", "result": "W", "score": "21-7", "margin": 14},
            {"date": "2026-09-25", "opponent": "Brockton", "result": "W", "score": "20-14", "margin": 6},
            {"date": "2026-10-02", "opponent": "Haverhill", "result": "W", "score": "34-28", "margin": 6},
            {"date": "2026-10-09", "opponent": "Bridgewater-Raynham", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-16", "opponent": "Barnstable", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-23", "opponent": "Dartmouth", "result": "W", "score": "24-10", "margin": 14}
        ],
        "next_game": "at Dartmouth (10/30)"
    },
    "Everett": {
        "mascot": "Crimson Tide", "colors": ["#990000", "#FFFFFF", "#FFD700"], "color_text": "Crimson, White, Gold",
        "record": "6-1", "wins": 6, "losses": 1, "rating": 10.3895, "avg_margin": 5.7143, "opp_rating": 4.6752,
        "scores": [
            {"date": "2026-09-11", "opponent": "Xaverian", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-18", "opponent": "Somerville", "result": "W", "score": "27-26", "margin": 1},
            {"date": "2026-09-25", "opponent": "Lynn English", "result": "W", "score": "35-12", "margin": 14},
            {"date": "2026-10-02", "opponent": "Medford", "result": "W", "score": "42-0", "margin": 14},
            {"date": "2026-10-09", "opponent": "Revere", "result": "W", "score": "38-7", "margin": 14},
            {"date": "2026-10-16", "opponent": "Malden", "result": "W", "score": "35-0", "margin": 14},
            {"date": "2026-10-23", "opponent": "Lynn Classical", "result": "W", "score": "28-14", "margin": 14}
        ],
        "next_game": "at Lynn Classical (10/30)"
    },
    "Methuen": {
        "mascot": "Rangers", "colors": ["#4169E1", "#FFFFFF"], "color_text": "Royal Blue, White",
        "record": "2-5", "wins": 2, "losses": 5, "rating": 8.8828, "avg_margin": -4.8571, "opp_rating": 13.7399,
        "scores": [
            {"date": "2026-09-11", "opponent": "Chelmsford", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-18", "opponent": "Billerica", "result": "L", "score": "21-35", "margin": -14},
            {"date": "2026-09-25", "opponent": "Haverhill", "result": "L", "score": "34-40", "margin": -6},
            {"date": "2026-10-02", "opponent": "Lawrence", "result": "W", "score": "42-12", "margin": 14},
            {"date": "2026-10-09", "opponent": "Andover", "result": "L", "score": "14-21", "margin": -7},
            {"date": "2026-10-16", "opponent": "Lowell", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-23", "opponent": "Central Catholic", "result": "L", "score": "10-31", "margin": -14}
        ],
        "next_game": "at Billerica (10/30)"
    },
    "Shrewsbury": {
        "mascot": "Colonials", "colors": ["#0A192F", "#C5B358"], "color_text": "Navy Blue, Vegas Gold",
        "record": "3-4", "wins": 3, "losses": 4, "rating": 8.5019, "avg_margin": -4.4286, "opp_rating": 12.9305,
        "scores": [
            {"date": "2026-09-11", "opponent": "Algonquin", "result": "W", "score": "27-18", "margin": 9},
            {"date": "2026-09-18", "opponent": "Grafton", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-25", "opponent": "Shepherd Hill", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-02", "opponent": "Wachusett", "result": "L", "score": "14-21", "margin": -7},
            {"date": "2026-10-09", "opponent": "Doherty", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-16", "opponent": "Leominster", "result": "L", "score": "21-40", "margin": -14},
            {"date": "2026-10-23", "opponent": "Westborough", "result": "L", "score": "14-28", "margin": -14}
        ],
        "next_game": "at Westborough (10/30)"
    },
    "Boston College High": {
        "mascot": "Eagles", "colors": ["#800000", "#FFD700"], "color_text": "Maroon, Gold",
        "record": "1-6", "wins": 1, "losses": 6, "rating": 8.2511, "avg_margin": -8.7143, "opp_rating": 16.9654,
        "scores": [
            {"date": "2026-09-11", "opponent": "La Salle (RI)", "result": "L", "score": "14-35", "margin": -14},
            {"date": "2026-09-18", "opponent": "Brockton", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-25", "opponent": "Malden Catholic", "result": "W", "score": "22-10", "margin": 12},
            {"date": "2026-10-02", "opponent": "Saint John's (Shrewsbury)", "result": "L", "score": "7-34", "margin": -14},
            {"date": "2026-10-09", "opponent": "Catholic Memorial", "result": "L", "score": "7-42", "margin": -14},
            {"date": "2026-10-16", "opponent": "Xaverian", "result": "L", "score": "6-47", "margin": -14},
            {"date": "2026-10-23", "opponent": "St. John's Prep", "result": "L", "score": "14-35", "margin": -14}
        ],
        "next_game": "vs. Saint John's (10/30)"
    },
    "Newton North": {
        "mascot": "Tigers", "colors": ["#FF6600", "#000000"], "color_text": "Orange, Black",
        "record": "6-1", "wins": 6, "losses": 1, "rating": 6.8728, "avg_margin": 6.7143, "opp_rating": 0.1585,
        "scores": [
            {"date": "2026-09-10", "opponent": "Waltham", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-09-18", "opponent": "Newton South", "result": "W", "score": "20-14", "margin": 6},
            {"date": "2026-09-25", "opponent": "Weymouth", "result": "W", "score": "14-12", "margin": 2},
            {"date": "2026-10-02", "opponent": "Framingham", "result": "W", "score": "29-18", "margin": 11},
            {"date": "2026-10-09", "opponent": "Natick", "result": "L", "score": "14-37", "margin": -14},
            {"date": "2026-10-16", "opponent": "Wellesley", "result": "W", "score": "31-6", "margin": 14},
            {"date": "2026-10-23", "opponent": "Cumberland (RI)", "result": "W", "score": "26-7", "margin": 14}
        ],
        "next_game": "at Braintree (10/30)"
    },
    "Weymouth": {
        "mascot": "Wildcats", "colors": ["#800000", "#FFD700"], "color_text": "Maroon, Gold",
        "record": "5-2", "wins": 5, "losses": 2, "rating": 6.5816, "avg_margin": 4.5714, "opp_rating": 2.0102,
        "scores": [
            {"date": "2026-09-11", "opponent": "Needham", "result": "W", "score": "33-15", "margin": 14},
            {"date": "2026-09-18", "opponent": "Brockton", "result": "L", "score": "8-21", "margin": -13},
            {"date": "2026-09-25", "opponent": "Newton North", "result": "L", "score": "12-14", "margin": -2},
            {"date": "2026-10-02", "opponent": "Framingham", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-09", "opponent": "Braintree", "result": "W", "score": "28-7", "margin": 14},
            {"date": "2026-10-16", "opponent": "Brookline", "result": "W", "score": "24-10", "margin": 14},
            {"date": "2026-10-23", "opponent": "Wellesley", "result": "W", "score": "21-14", "margin": 7}
        ],
        "next_game": "vs. Milton (10/29)"
    },
    "Lowell": {
        "mascot": "Red Raiders", "colors": ["#800000", "#FFFFFF"], "color_text": "Maroon, White",
        "record": "2-5", "wins": 2, "losses": 5, "rating": 6.1900, "avg_margin": -4.2857, "opp_rating": 10.4757,
        "scores": [
            {"date": "2026-09-11", "opponent": "Haverhill", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-18", "opponent": "Lawrence", "result": "W", "score": "46-0", "margin": 14},
            {"date": "2026-09-25", "opponent": "Billerica", "result": "L", "score": "18-41", "margin": -14},
            {"date": "2026-10-02", "opponent": "Chelmsford", "result": "L", "score": "12-28", "margin": -14},
            {"date": "2026-10-09", "opponent": "Central Catholic", "result": "L", "score": "7-35", "margin": -14},
            {"date": "2026-10-16", "opponent": "Methuen", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-23", "opponent": "Andover", "result": "L", "score": "14-35", "margin": -14}
        ],
        "next_game": "vs. North Andover (10/30)"
    },
    "Framingham": {
        "mascot": "Flyers", "colors": ["#0A192F", "#FFFFFF"], "color_text": "Navy Blue, White",
        "record": "4-3", "wins": 4, "losses": 3, "rating": 4.3554, "avg_margin": 0.5714, "opp_rating": 3.7840,
        "scores": [
            {"date": "2026-09-11", "opponent": "Durfee", "result": "W", "score": "28-27", "margin": 1},
            {"date": "2026-09-18", "opponent": "Brookline", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-09-25", "opponent": "Natick", "result": "W", "score": "28-10", "margin": 18},
            {"date": "2026-10-02", "opponent": "Newton North", "result": "L", "score": "18-29", "margin": -11},
            {"date": "2026-10-09", "opponent": "Weymouth", "result": "L", "score": "14-21", "margin": -7},
            {"date": "2026-10-16", "opponent": "Wellesley", "result": "W", "score": "24-14", "margin": 10},
            {"date": "2026-10-23", "opponent": "Milton", "result": "L", "score": "14-28", "margin": -14}
        ],
        "next_game": "vs. Needham (10/30)"
    },
    "Taunton": {
        "mascot": "Tigers", "colors": ["#FF6600", "#000000"], "color_text": "Orange, Black",
        "record": "3-4", "wins": 3, "losses": 4, "rating": 4.0806, "avg_margin": -1.2857, "opp_rating": 5.3663,
        "scores": [
            {"date": "2026-09-11", "opponent": "Attleboro", "result": "L", "score": "20-27", "margin": -7},
            {"date": "2026-09-18", "opponent": "New Bedford", "result": "L", "score": "7-21", "margin": -14},
            {"date": "2026-09-25", "opponent": "Stoughton", "result": "W", "score": "21-8", "margin": 13},
            {"date": "2026-10-02", "opponent": "Oliver Ames", "result": "W", "score": "28-7", "margin": 14},
            {"date": "2026-10-09", "opponent": "Canton", "result": "W", "score": "24-10", "margin": 14},
            {"date": "2026-10-16", "opponent": "Milford", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-23", "opponent": "Franklin", "result": "L", "score": "10-28", "margin": -14}
        ],
        "next_game": "vs. Franklin (10/30)"
    },
    "Durfee": {
        "mascot": "Hilltoppers", "colors": ["#CC0000", "#000000"], "color_text": "Red, Black",
        "record": "5-2", "wins": 5, "losses": 2, "rating": 3.9070, "avg_margin": 6.2857, "opp_rating": -2.3787,
        "scores": [
            {"date": "2026-09-11", "opponent": "New Bedford", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-18", "opponent": "TechBoston", "result": "W", "score": "34-7", "margin": 14},
            {"date": "2026-09-25", "opponent": "Framingham", "result": "L", "score": "27-28", "margin": -1},
            {"date": "2026-10-02", "opponent": "Brighton", "result": "W", "score": "42-0", "margin": 14},
            {"date": "2026-10-09", "opponent": "Brockton", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-16", "opponent": "East Boston", "result": "W", "score": "38-6", "margin": 14},
            {"date": "2026-10-23", "opponent": "Latin Academy", "result": "W", "score": "35-0", "margin": 14}
        ],
        "next_game": "vs. Brockton (10/30)"
    },
    "Attleboro": {
        "mascot": "Blue Bombardiers", "colors": ["#0033CC", "#C0C0C0", "#FFFFFF"], "color_text": "Blue, Silver, White",
        "record": "3-4", "wins": 3, "losses": 4, "rating": 3.1732, "avg_margin": -3.2857, "opp_rating": 6.4589,
        "scores": [
            {"date": "2026-09-11", "opponent": "Taunton", "result": "W", "score": "27-20", "margin": 7},
            {"date": "2026-09-18", "opponent": "King Philip", "result": "L", "score": "7-35", "margin": -14},
            {"date": "2026-09-25", "opponent": "Mansfield", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-02", "opponent": "North Attleborough", "result": "L", "score": "10-24", "margin": -14},
            {"date": "2026-10-09", "opponent": "Franklin", "result": "L", "score": "6-21", "margin": -14},
            {"date": "2026-10-16", "opponent": "Foxborough", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-23", "opponent": "Canton", "result": "W", "score": "28-10", "margin": 14}
        ],
        "next_game": "at Milford (10/30)"
    },
    "Acton-Boxborough": {
        "mascot": "Revolution", "colors": ["#0033CC", "#FFD700"], "color_text": "Blue, Gold",
        "record": "3-3", "wins": 3, "losses": 3, "rating": 3.0709, "avg_margin": 0.5000, "opp_rating": 2.5709,
        "scores": [
            {"date": "2026-09-11", "opponent": "Waltham", "result": "W", "score": "35-13", "margin": 14},
            {"date": "2026-09-18", "opponent": "Lincoln-Sudbury", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-09-25", "opponent": "Concord-Carlisle", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-02", "opponent": "Wayland", "result": "L", "score": "30-47", "margin": -14},
            {"date": "2026-10-09", "opponent": "Westford", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-16", "opponent": "Boston Latin", "result": "L", "score": "14-21", "margin": -7}
        ],
        "next_game": "at Bedford (10/30)"
    },
    "Needham": {
        "mascot": "Rockets", "colors": ["#0A192F", "#FFD700"], "color_text": "Navy Blue, Gold",
        "record": "1-6", "wins": 1, "losses": 6, "rating": 2.7401, "avg_margin": -8.7143, "opp_rating": 11.4544,
        "scores": [
            {"date": "2026-09-11", "opponent": "Natick", "result": "L", "score": "7-28", "margin": -14},
            {"date": "2026-09-18", "opponent": "Weymouth", "result": "L", "score": "15-33", "margin": -14},
            {"date": "2026-09-25", "opponent": "Braintree", "result": "W", "score": "21-7", "margin": 14},
            {"date": "2026-10-02", "opponent": "Milton", "result": "L", "score": "10-28", "margin": -14},
            {"date": "2026-10-09", "opponent": "Wellesley", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-16", "opponent": "Walpole", "result": "L", "score": "7-35", "margin": -14},
            {"date": "2026-10-23", "opponent": "Brookline", "result": "L", "score": "12-21", "margin": -9}
        ],
        "next_game": "at Framingham (10/30)"
    },
    "Arlington": {
        "mascot": "Spy Ponders", "colors": ["#800000", "#FFFFFF"], "color_text": "Maroon, White",
        "record": "2-5", "wins": 2, "losses": 5, "rating": 0.1879, "avg_margin": -3.8571, "opp_rating": 4.0451,
        "scores": [
            {"date": "2026-09-11", "opponent": "Woburn", "result": "L", "score": "0-7", "margin": -7},
            {"date": "2026-09-18", "opponent": "Winchester", "result": "L", "score": "14-38", "margin": -14},
            {"date": "2026-09-25", "opponent": "Melrose", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-02", "opponent": "Wakefield", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-09", "opponent": "Stoneham", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-16", "opponent": "Burlington", "result": "L", "score": "7-21", "margin": -14},
            {"date": "2026-10-23", "opponent": "Belmont", "result": "L", "score": "10-24", "margin": -14}
        ],
        "next_game": "vs. Lexington (Forfeit W)"
    },
    "Brookline": {
        "mascot": "Warriors", "colors": ["#800000", "#0A192F"], "color_text": "Maroon, Navy Blue",
        "record": "3-4", "wins": 3, "losses": 4, "rating": -1.7666, "avg_margin": -3.5714, "opp_rating": 1.8049,
        "scores": [
            {"date": "2026-09-11", "opponent": "Framingham", "result": "L", "score": "14-21", "margin": -7},
            {"date": "2026-09-18", "opponent": "Natick", "result": "L", "score": "6-27", "margin": -14},
            {"date": "2026-09-25", "opponent": "Braintree", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-02", "opponent": "Wellesley", "result": "L", "score": "10-28", "margin": -14},
            {"date": "2026-10-09", "opponent": "Newton South", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-16", "opponent": "Weymouth", "result": "L", "score": "10-24", "margin": -14},
            {"date": "2026-10-23", "opponent": "Needham", "result": "W", "score": "21-12", "margin": 9}
        ],
        "next_game": "at Wellesley (10/30)"
    },
    "Lawrence": {
        "mascot": "Lancers", "colors": ["#0A192F", "#FFFFFF"], "color_text": "Navy Blue, White",
        "record": "1-6", "wins": 1, "losses": 6, "rating": -3.8168, "avg_margin": -10.2857, "opp_rating": 6.4689,
        "scores": [
            {"date": "2026-09-11", "opponent": "Lowell", "result": "L", "score": "0-46", "margin": -14},
            {"date": "2026-09-18", "opponent": "Andover", "result": "L", "score": "0-42", "margin": -14},
            {"date": "2026-09-25", "opponent": "Chelmsford", "result": "L", "score": "6-35", "margin": -14},
            {"date": "2026-10-02", "opponent": "Methuen", "result": "L", "score": "12-42", "margin": -14},
            {"date": "2026-10-09", "opponent": "Haverhill", "result": "L", "score": "0-35", "margin": -14},
            {"date": "2026-10-16", "opponent": "Central Catholic", "result": "L", "score": "0-35", "margin": -14},
            {"date": "2026-10-23", "opponent": "Lynn Classical", "result": "W", "score": "21-14", "margin": 7}
        ],
        "next_game": "vs. Chelmsford (10/30)"
    },
    "Newton South": {
        "mascot": "Lions", "colors": ["#FF6600", "#4169E1"], "color_text": "Orange, Royal Blue",
        "record": "1-6", "wins": 1, "losses": 6, "rating": -6.9349, "avg_margin": -7.0000, "opp_rating": 0.0651,
        "scores": [
            {"date": "2026-09-11", "opponent": "Cambridge", "result": "L", "score": "20-21", "margin": -1},
            {"date": "2026-09-18", "opponent": "Newton North", "result": "L", "score": "14-20", "margin": -6},
            {"date": "2026-09-25", "opponent": "Weston", "result": "L", "score": "14-35", "margin": -14},
            {"date": "2026-10-02", "opponent": "Waltham", "result": "L", "score": "7-28", "margin": -14},
            {"date": "2026-10-09", "opponent": "Brookline", "result": "L", "score": "14-28", "margin": -14},
            {"date": "2026-10-16", "opponent": "Boston Latin", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-23", "opponent": "Wayland", "result": "L", "score": "10-24", "margin": -14}
        ],
        "next_game": "at Westford (10/30)"
    },
    "Braintree": {
        "mascot": "Wamps", "colors": ["#4169E1", "#FFFFFF"], "color_text": "Royal Blue, White",
        "record": "1-6", "wins": 1, "losses": 6, "rating": -5.6503, "avg_margin": -10.8571, "opp_rating": 5.2069,
        "scores": [
            {"date": "2026-09-11", "opponent": "Walpole", "result": "L", "score": "7-48", "margin": -14},
            {"date": "2026-09-18", "opponent": "Milton", "result": "L", "score": "0-35", "margin": -14},
            {"date": "2026-09-25", "opponent": "Needham", "result": "L", "score": "7-21", "margin": -14},
            {"date": "2026-10-02", "opponent": "Brookline", "result": "L", "score": "14-21", "margin": -7},
            {"date": "2026-10-09", "opponent": "Weymouth", "result": "L", "score": "7-28", "margin": -14},
            {"date": "2026-10-16", "opponent": "Wellesley", "result": "L", "score": "6-28", "margin": -14},
            {"date": "2026-10-23", "opponent": "Framingham", "result": "W", "score": "14-7", "margin": 7}
        ],
        "next_game": "vs. Newton North (10/30)"
    },
    "Belmont": {
        "mascot": "Marauders", "colors": ["#0A192F", "#800000"], "color_text": "Navy Blue, Maroon",
        "record": "2-5", "wins": 2, "losses": 5, "rating": -10.3076, "avg_margin": -7.1429, "opp_rating": -3.1647,
        "scores": [
            {"date": "2026-09-11", "opponent": "Reading", "result": "L", "score": "0-41", "margin": -14},
            {"date": "2026-09-18", "opponent": "Woburn", "result": "L", "score": "0-49", "margin": -14},
            {"date": "2026-09-25", "opponent": "Melrose", "result": "L", "score": "7-28", "margin": -14},
            {"date": "2026-10-02", "opponent": "Stoneham", "result": "W", "score": "21-14", "margin": 7},
            {"date": "2026-10-09", "opponent": "Wakefield", "result": "L", "score": "10-24", "margin": -14},
            {"date": "2026-10-16", "opponent": "Wilmington", "result": "W", "score": "28-14", "margin": 14},
            {"date": "2026-10-23", "opponent": "Arlington", "result": "W", "score": "24-10", "margin": 14}
        ],
        "next_game": "vs. Winchester (10/30)"
    },
    "Lexington": {
        "mascot": "Minutemen", "colors": ["#0033CC", "#FFD700"], "color_text": "Blue, Gold",
        "record": "0-7", "wins": 0, "losses": 7, "rating": -13.5601, "avg_margin": -14.0000, "opp_rating": 0.4399,
        "scores": [
            {"date": "2026-09-11", "opponent": "Reading", "result": "L", "score": "0-62", "margin": -14},
            {"date": "2026-09-18", "opponent": "Woburn", "result": "L", "score": "0-42", "margin": -14},
            {"date": "2026-09-25", "opponent": "Winchester", "result": "L", "score": "0-35", "margin": -14},
            {"date": "2026-10-02", "opponent": "Belmont", "result": "L", "score": "7-28", "margin": -14},
            {"date": "2026-10-09", "opponent": "Arlington", "result": "L", "score": "0-35", "margin": -14},
            {"date": "2026-10-16", "opponent": "Melrose", "result": "L", "score": "0-42", "margin": -14},
            {"date": "2026-10-23", "opponent": "Wakefield", "result": "L", "score": "0-28", "margin": -14}
        ],
        "next_game": "at Arlington (Forfeit L)"
    }
}

# --- PROCESS CURRENT STANDINGS & PLAYOFF ELIGIBILITY (AS OF NOW - 10/27) ---
rows = []
for school, data in teams_data.items():
    eligible = True if data["wins"] >= 3 else False
    rows.append({
        "School": school,
        "Mascot": data["mascot"],
        "Colors": data["color_text"],
        "Record": data["record"],
        "Wins": data["wins"],
        "Margin": data["avg_margin"],
        "SoS": data["opp_rating"],
        "Rating": data["rating"],
        "Eligible": eligible,
        "Next Game": data["next_game"]
    })

df = pd.DataFrame(rows).sort_values(by="Rating", ascending=False).reset_index(drop=True)

qualified_df = df[df["Eligible"] == True].reset_index(drop=True)
qualified_df.insert(0, "Seed", range(1, len(qualified_df) + 1))

# Navigation Tabs
tab_bracket, tab_inspector, tab_predict, tab_leaderboard = st.tabs([
    "🏆 Visual Playoff Bracket", "🔍 Team Inspector & Schedule", "🔮 Matchup Predictor", "📊 Master Leaderboard"
])

# --- TAB 1: VISUAL PLAYOFF BRACKET ---
with tab_bracket:
    st.header("🏆 Official MIAA Division 1 Playoff Bracket (As of Oct 27)")
    st.caption("Top 16 ELIGIBLE teams (with at least 3 wins). Methuen (2-5) and BC High (1-6) are currently ineligible, placing **Shrewsbury at Seed #15** and **Newton North at Seed #16**.")

    top16 = qualified_df.head(16)
    
    pairings = [
        (1, 16), (8, 9), (5, 12), (4, 13),
        (3, 14), (6, 11), (7, 10), (2, 15)
    ]

    st.subheader("Round 1 Postseason Matchup Tree")
    
    col_left, col_right = st.columns(2)
    
    for idx, (s1, s2) in enumerate(pairings):
        t1_row = top16[top16["Seed"] == s1].iloc[0] if len(top16[top16["Seed"] == s1]) > 0 else None
        t2_row = top16[top16["Seed"] == s2].iloc[0] if len(top16[top16["Seed"] == s2]) > 0 else None
        
        target_col = col_left if idx < 4 else col_right
        
        with target_col:
            if t1_row is not None and t2_row is not None:
                m1_color = teams_data[t1_row["School"]]["colors"][0]
                m2_color = teams_data[t2_row["School"]]["colors"][0]
                
                st.markdown(f"""
                <div class="matchup-card">
                    <div style="font-size: 0.8rem; color: #94A3B8; font-weight: bold; margin-bottom: 6px;">
                        ROUND 1 MATCHUP #{idx+1}
                    </div>
                    <div class="team-row">
                        <span class="team-badge">
                            <span class="seed-tag">#{t1_row['Seed']}</span>
                            <span class="color-pill" style="background-color: {m1_color};"></span>
                            {t1_row['School']} <span class="mascot-tag">({t1_row['Mascot']})</span>
                        </span>
                        <span class="rating-val">{t1_row['Rating']:.4f}</span>
                    </div>
                    <div style="text-align: center; color: #64748B; font-weight: bold; font-size: 0.75rem; margin: 2px 0;">VS</div>
                    <div class="team-row">
                        <span class="team-badge">
                            <span class="seed-tag">#{t2_row['Seed']}</span>
                            <span class="color-pill" style="background-color: {m2_color};"></span>
                            {t2_row['School']} <span class="mascot-tag">({t2_row['Mascot']})</span>
                        </span>
                        <span class="rating-val">{t2_row['Rating']:.4f}</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# --- TAB 2: TEAM INSPECTOR & SCHEDULE ---
with tab_inspector:
    st.header("🔍 Team Inspector, Mascot, Colors & Game History")
    selected_team = st.selectbox("Select Team to Inspect:", sorted(list(teams_data.keys())))
    
    if selected_team:
        t = teams_data[selected_team]
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Mascot", t["mascot"])
        c2.metric("Team Colors", t["color_text"])
        c3.metric("Record", t["record"])
        c4.metric("MIAA Rating", f"{t['rating']:.4f}")
        
        st.subheader(f"📅 Chronological Schedule & Scores ({selected_team})")
        
        for game in t["scores"]:
            badge = "🟢 W" if game["result"] == "W" else "🔴 L"
            st.markdown(f"**{game['date']}** — {badge} **{game['score']}** vs **{game['opponent']}** *(Margin: {game['margin']:+} pts)*")
        
        st.info(f"**Next Week 8 Matchup**: {t['next_game']}")

# --- TAB 3: MATCHUP PREDICTOR ---
with tab_predict:
    st.header("🔮 Mathematical Win Probability & Score Predictor")
    st.write("Predicts win likelihood and score spread using MIAA rating differentials and capped victory margins.")
    
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        team_a = st.selectbox("Select Team A:", sorted(list(teams_data.keys())), index=sorted(list(teams_data.keys())).index("Newton North"))
    with p_col2:
        team_b = st.selectbox("Select Team B:", sorted(list(teams_data.keys())), index=sorted(list(teams_data.keys())).index("Saint John's (Shrewsbury)"))
    
    if team_a and team_b and team_a != team_b:
        r_a = teams_data[team_a]["rating"]
        r_b = teams_data[team_b]["rating"]
        diff = r_a - r_b
        
        import math
        prob_a = 1.0 / (1.0 + math.pow(10, -diff / 10.0))
        prob_b = 1.0 - prob_a
        
        st.subheader("Matchup Prediction Analysis")
        
        m_col1, m_col2 = st.columns(2)
        m_col1.metric(f"{team_a} Win Chance", f"{prob_a*100:.1f}%")
        m_col2.metric(f"{team_b} Win Chance", f"{prob_b*100:.1f}%")
        
        proj_margin = round(diff * 0.75)
        if proj_margin > 0:
            st.success(f"**Predicted Outcome**: **{team_a}** favored by **{abs(proj_margin)} points** over {team_b}.")
        elif proj_margin < 0:
            st.success(f"**Predicted Outcome**: **{team_b}** favored by **{abs(proj_margin)} points** over {team_a}.")
        else:
            st.info("**Predicted Outcome**: Evenly matched toss-up game!")

# --- TAB 4: MASTER LEADERBOARD ---
with tab_leaderboard:
    st.header("📊 Full MIAA Division 1 Master Leaderboard (1–33)")
    all_df = df.copy()
    all_df.insert(0, "Rank #", range(1, len(all_df) + 1))
    
    st.dataframe(
        all_df[["Rank #", "School", "Mascot", "Colors", "Record", "Margin", "SoS", "Rating", "Eligible"]],
        column_config={
            "Rank #": st.column_config.NumberColumn("Rank", width="small"),
            "Margin": st.column_config.NumberColumn("Avg Margin", format="%+.4f"),
            "SoS": st.column_config.NumberColumn("Opponent Rating", format="%.4f"),
            "Rating": st.column_config.NumberColumn("MIAA Rating", format="%.4f")
        },
        hide_index=True,
        use_container_width=True
    )
