import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(
    page_title="MIAA D1 Football Tracker & Simulator",
    layout="wide",
    page_icon="🏈",
)
st.title("🏈 MIAA Division 1 Football Leaderboard & Playoff Simulator")
st.caption(
    "Official MIAA Ratings & Standings (As of October 27) • "
    "Interactive Team Inspector & Postseason Bracket"
)

# --- 1. FULL 33-TEAM DIVISION 1 DATABASE ---
teams_data = {"St. John's Prep": {'record': '7-0',
                     'wins': 7,
                     'losses': 0,
                     'rating': 27.798,
                     'avg_margin': 12.5714,
                     'opp_rating': 15.2266,
                     'scores': ['W 31-12 vs Malden Catholic',
                                "W 43-20 vs Saint John's",
                                'W 35-21 vs Catholic Memorial'],
                     'next_game': 'at Catholic Memorial (10/30)'},
 "Saint John's (Shrewsbury)": {'record': '6-1',
                               'wins': 6,
                               'losses': 1,
                               'rating': 25.9005,
                               'avg_margin': 10.0,
                               'opp_rating': 15.9005,
                               'scores': ['W 34-7 vs Catholic Memorial',
                                          'W 27-18 vs Algonquin',
                                          "L 20-43 at St. John's Prep"],
                               'next_game': 'at BC High (10/30)'},
 'Central Catholic': {'record': '4-3',
                      'wins': 4,
                      'losses': 3,
                      'rating': 23.6116,
                      'avg_margin': 3.4286,
                      'opp_rating': 20.1831,
                      'scores': ['W 42-24 at Andover', 'L 27-28 vs Londonderry (NH)'],
                      'next_game': 'vs. Haverhill (10/29)'},
 'Springfield Central': {'record': '6-1',
                         'wins': 6,
                         'losses': 1,
                         'rating': 20.5456,
                         'avg_margin': 9.0,
                         'opp_rating': 11.5456,
                         'scores': ['W 55-14 vs East Longmeadow', 'W 42-14 vs West Springfield'],
                         'next_game': 'at West Springfield (10/30)'},
 'Wachusett Regional': {'record': '7-0',
                        'wins': 7,
                        'losses': 0,
                        'rating': 20.2372,
                        'avg_margin': 11.0,
                        'opp_rating': 9.2372,
                        'scores': ['W 38-0 at Grafton', 'W 42-0 vs Westborough'],
                        'next_game': 'at Algonquin (10/30)'},
 'Xaverian Brothers': {'record': '3-4',
                       'wins': 3,
                       'losses': 4,
                       'rating': 17.7758,
                       'avg_margin': -0.2857,
                       'opp_rating': 18.0616,
                       'scores': ['W 47-6 at BC High', 'L 21-42 vs Catholic Memorial'],
                       'next_game': 'vs. Malden Catholic (10/30)'},
 'Andover': {'record': '5-2',
             'wins': 5,
             'losses': 2,
             'rating': 16.3508,
             'avg_margin': 3.7143,
             'opp_rating': 12.6365,
             'scores': ['L 24-42 vs Central Catholic', 'W 36-29 vs Pinkerton (NH)'],
             'next_game': 'at Tewksbury (10/30)'},
 'Franklin': {'record': '5-2',
              'wins': 5,
              'losses': 2,
              'rating': 16.0439,
              'avg_margin': 5.4286,
              'opp_rating': 10.6153,
              'scores': ['L 6-41 at Milton', 'W 21-6 vs Attleboro'],
              'next_game': 'at Taunton (10/30)'},
 'Leominster': {'record': '4-3',
                'wins': 4,
                'losses': 3,
                'rating': 15.3921,
                'avg_margin': 3.2857,
                'opp_rating': 12.1064,
                'scores': ['W 21-7 vs Westborough', 'W 40-21 vs Shrewsbury'],
                'next_game': 'at Grafton (10/30)'},
 'Brockton': {'record': '3-4',
              'wins': 3,
              'losses': 4,
              'rating': 10.8963,
              'avg_margin': -1.7143,
              'opp_rating': 12.6106,
              'scores': ['L 14-20 vs New Bedford', 'W 21-8 vs Weymouth'],
              'next_game': 'at Durfee (10/30)'},
 'Natick': {'record': '4-3',
            'wins': 4,
            'losses': 3,
            'rating': 10.8125,
            'avg_margin': 2.1429,
            'opp_rating': 8.6697,
            'scores': ['W 37-14 vs Wellesley', 'W 27-6 vs Brookline', 'W 37-14 vs Newton North'],
            'next_game': 'at Walpole (10/30)'},
 'Haverhill': {'record': '5-2',
               'wins': 5,
               'losses': 2,
               'rating': 10.6868,
               'avg_margin': 6.0,
               'opp_rating': 4.6868,
               'scores': ['W 40-34 vs Methuen', 'L 28-34 vs New Bedford'],
               'next_game': 'at Central Catholic (10/29)'},
 'New Bedford': {'record': '6-1',
                 'wins': 6,
                 'losses': 1,
                 'rating': 10.4183,
                 'avg_margin': 7.2857,
                 'opp_rating': 3.1326,
                 'scores': ['W 20-14 at Brockton', 'W 34-28 at Haverhill'],
                 'next_game': 'at Dartmouth (10/30)'},
 'Everett': {'record': '6-1',
             'wins': 6,
             'losses': 1,
             'rating': 10.3895,
             'avg_margin': 5.7143,
             'opp_rating': 4.6752,
             'scores': ['W 27-26 vs Somerville', 'W 35-12 vs Lynn English'],
             'next_game': 'at Lynn Classical (10/30)'},
 'Methuen': {'record': '2-5',
             'wins': 2,
             'losses': 5,
             'rating': 8.8828,
             'avg_margin': -4.8571,
             'opp_rating': 13.7399,
             'scores': ['L 34-40 at Haverhill', 'W 42-12 vs Lawrence'],
             'next_game': 'at Billerica (10/30)'},
 'Shrewsbury': {'record': '3-4',
                'wins': 3,
                'losses': 4,
                'rating': 8.5019,
                'avg_margin': -4.4286,
                'opp_rating': 12.9305,
                'scores': ['W 27-18 vs Algonquin', 'L 21-40 at Leominster'],
                'next_game': 'at Westborough (10/30)'},
 'Boston College High': {'record': '1-6',
                         'wins': 1,
                         'losses': 6,
                         'rating': 8.2511,
                         'avg_margin': -8.7143,
                         'opp_rating': 16.9654,
                         'scores': ['L 6-47 vs Xaverian', 'W 22-10 vs Malden Catholic'],
                         'next_game': "vs. Saint John's (10/30)"},
 'Newton North': {'record': '6-1',
                  'wins': 6,
                  'losses': 1,
                  'rating': 6.8728,
                  'avg_margin': 6.7143,
                  'opp_rating': 0.1585,
                  'scores': ['W 28-14 vs Waltham',
                             'W 20-14 vs Newton South',
                             'W 14-12 vs Weymouth',
                             'W 29-18 vs Framingham',
                             'L 14-37 vs Natick',
                             'W 31-6 vs Wellesley',
                             'W 26-7 vs Cumberland (RI)'],
                  'next_game': 'at Braintree (10/30)'},
 'Weymouth': {'record': '5-2',
              'wins': 5,
              'losses': 2,
              'rating': 6.5816,
              'avg_margin': 4.5714,
              'opp_rating': 2.0102,
              'scores': ['W 33-15 at Needham', 'L 8-21 vs Brockton', 'L 12-14 at Newton North'],
              'next_game': 'vs. Milton (10/29)'},
 'Lowell': {'record': '2-5',
            'wins': 2,
            'losses': 5,
            'rating': 6.19,
            'avg_margin': -4.2857,
            'opp_rating': 10.4757,
            'scores': ['W 46-0 at Lawrence', 'L 18-41 vs Billerica'],
            'next_game': 'vs. North Andover (10/30)'},
 'Framingham': {'record': '4-3',
                'wins': 4,
                'losses': 3,
                'rating': 4.3554,
                'avg_margin': 0.5714,
                'opp_rating': 3.784,
                'scores': ['W 28-27 vs Durfee', 'L 18-29 at Newton North'],
                'next_game': 'vs. Needham (10/30)'},
 'Taunton': {'record': '3-4',
             'wins': 3,
             'losses': 4,
             'rating': 4.0806,
             'avg_margin': -1.2857,
             'opp_rating': 5.3663,
             'scores': ['L 20-27 at Attleboro', 'W 21-8 vs Stoughton'],
             'next_game': 'vs. Franklin (10/30)'},
 'Durfee': {'record': '5-2',
            'wins': 5,
            'losses': 2,
            'rating': 3.907,
            'avg_margin': 6.2857,
            'opp_rating': -2.3787,
            'scores': ['W 34-7 at TechBoston', 'L 27-28 at Framingham'],
            'next_game': 'vs. Brockton (10/30)'},
 'Attleboro': {'record': '3-4',
               'wins': 3,
               'losses': 4,
               'rating': 3.1732,
               'avg_margin': -3.2857,
               'opp_rating': 6.4589,
               'scores': ['W 27-20 vs Taunton', 'L 6-21 vs Franklin'],
               'next_game': 'at Milford (10/30)'},
 'Acton-Boxborough': {'record': '3-3',
                      'wins': 3,
                      'losses': 3,
                      'rating': 3.0709,
                      'avg_margin': 0.5,
                      'opp_rating': 2.5709,
                      'scores': ['W 35-13 at Waltham', 'L 30-47 vs Wayland'],
                      'next_game': 'at Bedford (10/30)'},
 'Needham': {'record': '1-6',
             'wins': 1,
             'losses': 6,
             'rating': 2.7401,
             'avg_margin': -8.7143,
             'opp_rating': 11.4544,
             'scores': ['L 15-33 vs Weymouth', 'W 21-7 vs Braintree'],
             'next_game': 'at Framingham (10/30)'},
 'Arlington': {'record': '2-5',
               'wins': 2,
               'losses': 5,
               'rating': 0.1879,
               'avg_margin': -3.8571,
               'opp_rating': 4.0451,
               'scores': ['L 0-7 vs Woburn', 'L 14-38 vs Winchester'],
               'next_game': 'vs. Lexington (Forfeit W)'},
 'Brookline': {'record': '3-4',
               'wins': 3,
               'losses': 4,
               'rating': -1.7666,
               'avg_margin': -3.5714,
               'opp_rating': 1.8049,
               'scores': ['L 6-27 at Natick'],
               'next_game': 'at Wellesley (10/30)'},
 'Lawrence': {'record': '1-6',
              'wins': 1,
              'losses': 6,
              'rating': -3.8168,
              'avg_margin': -10.2857,
              'opp_rating': 6.4689,
              'scores': ['L 0-46 vs Lowell', 'L 12-42 at Methuen'],
              'next_game': 'vs. Chelmsford (10/30)'},
 'Braintree': {'record': '1-6',
               'wins': 1,
               'losses': 6,
               'rating': -5.6503,
               'avg_margin': -10.8571,
               'opp_rating': 5.2069,
               'scores': ['L 7-48 vs Walpole', 'L 7-21 at Needham'],
               'next_game': 'vs. Newton North (10/30)'},
 'Newton South': {'record': '1-6',
                  'wins': 1,
                  'losses': 6,
                  'rating': -6.9349,
                  'avg_margin': -7.0,
                  'opp_rating': 0.0651,
                  'scores': ['L 20-21 vs Cambridge',
                             'L 14-35 vs Weston',
                             'L 14-20 at Newton North'],
                  'next_game': 'at Westford (10/30)'},
 'Belmont': {'record': '2-5',
             'wins': 2,
             'losses': 5,
             'rating': -10.3076,
             'avg_margin': -7.1429,
             'opp_rating': -3.1647,
             'scores': ['L 0-41 at Reading', 'L 0-49 vs Woburn'],
             'next_game': 'vs. Winchester (10/30)'},
 'Lexington': {'record': '0-7',
               'wins': 0,
               'losses': 7,
               'rating': -13.5601,
               'avg_margin': -14.0,
               'opp_rating': 0.4399,
               'scores': ['L 0-62 vs Reading'],
               'next_game': 'at Arlington (Forfeit L)'}}

# --- 2. TEAM INSPECTOR ---
st.header("🔍 Team Inspector")
selected_team = st.selectbox(
    "Select any Division 1 School:",
    sorted(teams_data.keys()),
)

if selected_team:
    team = teams_data[selected_team]
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("W-L Record", team["record"])
    c2.metric("Overall MIAA Rating", f'{team["rating"]:.4f}')
    c3.metric("Avg Victory Margin", f'{team["avg_margin"]:+.4f}')
    c4.metric("Opponent Rating (SoS)", f'{team["opp_rating"]:.4f}')
    c5.metric("Week 8 Matchup", team["next_game"])

    st.subheader(f"Game History for {selected_team}")
    if team["scores"]:
        for score in team["scores"]:
            st.write(f"• {score}")
    else:
        st.write("No score details logged.")

st.divider()

# --- 3. PLAYOFF BRACKET SIMULATION ---
st.header("🏆 Projected Postseason Bracket (Top 16)")
st.write(
    "Applying MIAA Postseason Rules: Teams MUST achieve **at least 3 wins** to qualify. "
    "Assuming teams currently with 2 wins (like Methuen and Lowell) lose in Week 8, "
    "they finish 2–6 and are **automatically eliminated**."
)

# Build standings table
rows = []
for team_name, data in teams_data.items():
    eligible = data["wins"] >= 3
    rows.append(
        {
            "School": team_name,
            "Record": data["record"],
            "Wins": data["wins"],
            "Margin": data["avg_margin"],
            "SoS": data["opp_rating"],
            "Rating": data["rating"],
            "Eligible": eligible,
            "Next Game": data["next_game"],
        }
    )

df = (
    pd.DataFrame(rows)
    .sort_values(by="Rating", ascending=False)
    .reset_index(drop=True)
)
qualified_df = df[df["Eligible"]].reset_index(drop=True)

# Display top 16 seeds
st.dataframe(
    qualified_df[["School", "Record", "Margin", "SoS", "Rating", "Next Game"]].head(16),
    column_config={
        "School": "School Name",
        "Record": "W-L",
        "Margin": st.column_config.NumberColumn(
            "Avg Margin (+/-14 Cap)", format="%+.4f"
        ),
        "SoS": st.column_config.NumberColumn("Opponent Rating", format="%.4f"),
        "Rating": st.column_config.NumberColumn("Overall Rating", format="%.4f"),
        "Next Game": "Week 8 Matchup",
    },
    use_container_width=True,
)

st.divider()

# --- 4. BUBBLE WATCH ---
st.header("🫧 Playoff Bubble & Cutoff Watch")
col_in, col_out = st.columns(2)

with col_in:
    st.subheader("Last Seeds In (Seeds #14–#16)")
    st.dataframe(
        qualified_df[["School", "Record", "Rating", "Next Game"]].iloc[13:16],
        column_config={
            "Rating": st.column_config.NumberColumn("MIAA Rating", format="%.4f")
        },
        use_container_width=True,
    )

with col_out:
    st.subheader("Disqualified / Eliminated (Under 3 Wins)")
    eliminated_df = df[~df["Eligible"]].reset_index(drop=True)
    eliminated_df.index += 1
    st.dataframe(
        eliminated_df[["School", "Record", "Wins", "Rating", "Next Game"]],
        column_config={
            "Rating": st.column_config.NumberColumn("MIAA Rating", format="%.4f")
        },
        use_container_width=True,
    )

st.divider()

# --- 5. FULL DIVISION 1 STANDINGS (ALL 33 TEAMS) ---
st.header("📊 Full MIAA Division 1 Master Leaderboard (1–33)")
all_df = df.copy()
all_df.index += 1
st.dataframe(
    all_df[["School", "Record", "Margin", "SoS", "Rating", "Eligible"]],
    column_config={
        "Margin": st.column_config.NumberColumn("Avg Margin", format="%+.4f"),
        "SoS": st.column_config.NumberColumn("Opponent Rating", format="%.4f"),
        "Rating": st.column_config.NumberColumn("Overall Rating", format="%.4f"),
    },
    use_container_width=True,
)
