import streamlit as st
from datetime import datetime


st.set_page_config(
    page_icon="🔮",
    layout="centered",  # 改为居中布局（替代wide）
    initial_sidebar_state="collapsed"
)


st.markdown("""
    <style>
    /* 全局背景 & 文字（匹配第二张图的深色风格） */
    .stApp {
        background-color: #000000;  /* 纯黑背景 */
        color: #e0e0e0;
    }
    /* 容器宽度限制（缩小内容宽度） */
    .main .block-container {
        max-width: 600px !important;  /* 固定窄宽度 */
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    /* 标题/头部样式（统一紫色系） */
    .css-10trblm { color: #a371f7; } /* title */
    .css-1v0mbdj { color: #a371f7; } /* header */
    /* metric样式（技能矩阵，紧凑卡片） */
    .css-1x8cf1d { 
        background-color: #1a1a2e;  /* 深紫背景 */
        padding: 0.5rem; 
        border-radius: 4px; 
        margin-bottom: 0.5rem;
    }
    .css-1x8cf1d .css-10kw83r { color: #e0e0e0; } /* metric标题 */
    .css-1x8cf1d .css-1n543e5 { color: #ffffff; font-size: 1.2rem; } /* 缩小数值字体 */
    /* table样式（任务日志，紧凑表格） */
    table {
        width: 100%;
        border-collapse: collapse;
        background-color: #1a1a2e;
        border-radius: 4px;
        font-size: 0.9rem;  /* 缩小表格字体 */
    }
    th, td {
        padding: 0.5rem;  /* 紧凑内边距 */
        text-align: left;
        border-bottom: 1px solid #2a3346;
    }
    th {
        color: #a371f7;
    }
    /* code块样式（深色背景） */
    .css-1kyxreq { 
        background-color: #1a1a2e; 
        border-radius: 4px; 
        font-size: 0.8rem;  /* 缩小代码字体 */
    }
    /* 状态标签（匹配第二张图的颜色） */
    .status-doing { color: #4ade80; font-weight: bold; }
    .status-fail { color: #f87171; font-weight: bold; }
    /* 底部系统提示（缩小字体） */
    .system-msg { color: #9ca3af; font-size: 0.75rem; }
    /* 进度条样式优化 */
    .progress-bar {
        background-color: #1a1a2e;
        padding: 0.3rem;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)



st.title("🥭芒果 热播剧 - 流量档案")


st.header("🍌 基础信息")
# 紧凑显示基础信息（用小字体）
st.markdown("""
<div style="font-size: 0.9rem;">
- 管理ID: NO-2023-001<br>
- 注册时间: 2023-01-01 | 精神状态: ♈ 正常<br>
- 出勤情况: ✅安全出勤
</div>
""", unsafe_allow_html=True)


st.header("🍓️ 流量矩阵")
# 缩小列间距，紧凑显示
col1, col2, col3 = st.columns([1,1,1], gap="small")
with col1:
    st.metric(label="TV", value="80%", delta="+2%")
with col2:
    st.metric(label="movin", value="54%", delta="+2%")
with col3:
    st.metric(label="zy", value="68%", delta="+27%")


st.header("🥭 芒果TV爆剧进度")
# 紧凑进度条
st.markdown("""
<div class="progress-bar">
    <div style="width: 80%; background: linear-gradient(90deg, #61dafb, #a371f7); height: 6px; border-radius: 3px;"></div>
    <p style="margin-top: 0.3rem; color: #e0e0e0; font-size: 0.9rem;">80% 完成</p>
</div>
""", unsafe_allow_html=True)



st.header("☕ 上线日期")
task_data = [
    ["2025-11-01", "入青云", '<span class="status-doing">已完成</span>', "★★★★★"],
    ["2025-11-05", "一笑随歌", '<span class="status-doing">进行中</span>', "★★★☆"],
    ["2025-12-12", "现在就出发3", '<span class="status-fail">未完成</span>', "★★★★☆"]
]

# 修复表格标签错误，紧凑显示
st.markdown(f"""
<table>
    <thead>
        <tr>
            <<th>日期</</th>
            <<th>剧名</</th>
            <<th>进度</</th>
            <<th>流量</</th>
        </tr>
    </thead>
    <tbody>
        {''.join([f'<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>' for row in task_data])}
    </tbody>
</table>
""", unsafe_allow_html=True)


st.header("😮💨 最新数据成果")
# 缩小代码块
code_content = '''
def user_verify():
    if request.values.get("verify"):
        explet = "ACCESS GRANTED"
        st.write(explet)
'''
st.code(code_content, language="python")



st.markdown("""
<div class="system-msg">
    😜 SYSTEM MESSAGE: 下一个热播剧正在准备。<br>
    🤭 WARNING: 请防沉迷观看<br>
    🥭 TIMESTAMP: 2025-12-18 15:45:48<br>
    系统状态: 😎在线 | 数据状态: 😪已加密
</div>
""", unsafe_allow_html=True)
