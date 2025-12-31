import streamlit as st
import pandas as pd
import altair as alt

# 页面配置
st.set_page_config(
    page_title="学生成绩分析与预测系统",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 初始化 session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = '项目概述'

# 侧边栏导航
with st.sidebar:
    st.header("导航航菜单")
    
    
    # 使用 radio 单选按钮
    page = st.radio(
        "选择页面",
        ["项目介绍", "专业数据分析", "成绩预测"],
        label_visibility="collapsed"
    )
    
    # 更新当前页面
    if page == "项目介绍":
        st.session_state.current_page = '项目概述'
    elif page == "专业数据分析":
        st.session_state.current_page = '数据分析'
    elif page == "成绩预测":
        st.session_state.current_page = '模型预测'

# 初始化图片索引
if 'image_index' not in st.session_state:
    st.session_state.image_index = 0

# 根据选择的页面显示不同内容
if st.session_state.current_page == '项目概述':
    # 主标题
    st.title("📊 学生成绩分析与预测系统")
    st.divider()
    
    st.header("📋 项目概述")
    
    # 创建两列布局：左侧内容，右侧图片
    col_content, col_image = st.columns([2, 1])
    
    with col_content:
        st.write("""
        本项目是一个基于Python和Streamlit开发的数据分析系统，采用机器学习算法对学生成绩进行分析，
        预测未来成绩趋势并为教学决策提供支持。系统整合了多种数据分析工具，为用户提供直观、高效的分析体验。
        """)
        
        st.subheader("主要特点：")
        st.write("- 📊 **数据可视化**：使用Plotly生成交互式图表，直观展示成绩分布")
        st.write("- 🔍 **成绩分析**：深入分析各科成绩的相关性和趋势")
        st.write("- 🎯 **智能预测**：基于多种机器学习算法进行成绩预测")
        st.write("- 📈 **多维分析**：提供成绩分布、趋势分析等多个分析维度")
    
    with col_image:
        # 图片展示区域
        with st.container(border=True):
            st.write(f"当前图片 {st.session_state.image_index + 1}")
            
            # 显示对应的图片
            image_files = ['1.png', '2.png', '3.png']
            st.image(image_files[st.session_state.image_index])
            
            # 图片切换按钮
            col_prev, col_next = st.columns(2)
            with col_prev:
                if st.button("⬅️ 上一页", use_container_width=True):
                    if st.session_state.image_index > 0:
                        st.session_state.image_index -= 1
                        st.rerun()
            with col_next:
                if st.button("下一页 ➡️", use_container_width=True):
                    if st.session_state.image_index < 2:
                        st.session_state.image_index += 1
                        st.rerun()
    
    st.divider()
    
    st.header("项目目标*")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🎯 目标一")
        st.write("**提升教学质量**")
        st.write("- 识别薄弱学科和知识点")
        st.write("- 个性化教学方案设计")
        st.write("- 动态调整教学策略")
    
    with col2:
        st.subheader("📊 目标二")
        st.write("**预测成绩趋势**")
        st.write("- 预测学生未来成绩")
        st.write("- 科学成绩评估")
        st.write("- 早期预警机制")
    
    with col3:
        st.subheader("📈 目标三")
        st.write("**优化管理决策**")
        st.write("- 数据驱动决策")
        st.write("- 可视化报告")
        st.write("- 支持长期规划")
    
    st.divider()
    
    st.header("🛠️ 技术架构")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        with st.container(border=True):
            st.write("**前端框架**")
            st.write("Streamlit")
            st.write("Python")
    
    with col2:
        with st.container(border=True):
            st.write("**数据处理**")
            st.write("Pandas")
            st.write("NumPy")
    
    with col3:
        with st.container(border=True):
            st.write("**可视化**")
            st.write("Plotly")
            st.write("Matplotlib")
    
    with col4:
        with st.container(border=True):
            st.write("**机器学习**")
            st.write("Scikit-Learn")

elif st.session_state.current_page == '数据分析':
    
    st.header("📊 专业数据分析")
    
    # 读取数据
    try:
        df = pd.read_csv('student_data_adjusted_rounded.csv')
        
        # 1. 各专业男女性别比例
        st.subheader("1. 各专业男女性别比例")
        
        col_chart1, col_table1 = st.columns([2, 1])
        
        with col_chart1:
            st.write("各专业男女性别统计")
            # 按专业和性别统计人数
            gender_major = df.groupby(['专业', '性别']).size().unstack(fill_value=0)
            # 计算比例
            gender_ratio = gender_major.div(gender_major.sum(axis=1), axis=0)
            gender_ratio = gender_ratio.reset_index()
            gender_ratio.columns = ['专业', '男性比例', '女性比例']
            
            # 转换为长格式
            gender_long = gender_ratio.melt(id_vars=['专业'], var_name='性别', value_name='比例')
            
            # 使用 Altair 创建分组柱状图
            chart = alt.Chart(gender_long).mark_bar(size=30).encode(
                x=alt.X('性别:N', title=None, axis=alt.Axis(labels=False, ticks=False)),
                y=alt.Y('比例:Q', title='比例', scale=alt.Scale(domain=[0, 0.6])),
                color=alt.Color('性别:N', scale=alt.Scale(domain=['男性比例', '女性比例'], range=['#1f77b4', '#5dade2']), legend=alt.Legend(title='性别')),
                column=alt.Column('专业:N', title='专业', header=alt.Header(labelOrient='bottom'))
            ).properties(
                width=120,
                height=400
            )
            
            st.altair_chart(chart)
        
        with col_table1:
            st.write("性别比例数据")
            # 计算每个专业的性别比例
            gender_major = df.groupby(['专业', '性别']).size().unstack(fill_value=0)
            gender_ratio = gender_major.div(gender_major.sum(axis=1), axis=0).round(4)
            gender_ratio.columns = ['男', '女']
            st.dataframe(gender_ratio, use_container_width=True)
        
        st.divider()
        
        # 2. 各专业学习指标对比
        st.subheader("2. 各专业学习指标对比")
        
        col_chart2, col_table2 = st.columns([2, 1])
        
        with col_chart2:
            st.write("各专业期中期末成绩趋势")
            # 按专业计算平均值
            major_avg = df.groupby('专业')[['期中考试分数', '期末考试分数', '每周学习时长（小时）']].mean().reset_index()
            
            # 考试分数折线图（左Y轴）
            score_long = major_avg.melt(id_vars=['专业'], value_vars=['期中考试分数', '期末考试分数'], var_name='考试类型', value_name='分数')
            
            line_score = alt.Chart(score_long).mark_line(point=True).encode(
                x=alt.X('专业:N', title='专业'),
                y=alt.Y('分数:Q', title='分数', scale=alt.Scale(domain=[71, 76])),
                color=alt.Color('考试类型:N', scale=alt.Scale(domain=['期中考试分数', '期末考试分数','每周学习时间'], range=['#1f77b4', '#5dade2','#e74c3c']), legend=alt.Legend(title='考试类型'))
            )
            
            # 每周学习时长折线图（右Y轴）
            line_study = alt.Chart(major_avg).mark_line(point=True, color='#e74c3c').encode(
                x=alt.X('专业:N', title='专业'),
                y=alt.Y('每周学习时长（小时）:Q', title='每周学习时长（小时）', scale=alt.Scale(domain=[20, 20.2])),
            )
            
            # 合并两个图表
            combined_chart = alt.layer(line_score, line_study).resolve_scale(
                y='independent'
            ).properties(
                height=400
            )
            
            st.altair_chart(combined_chart, use_container_width=True)
        
        with col_table2:
            st.write("详细数据")
            # 显示详细统计数据
            major_detail = df.groupby('专业')[['期中考试分数', '期末考试分数', '每周学习时长（小时）']].mean().round(4)
            st.dataframe(major_detail, use_container_width=True)
        
        st.divider()
        
        # 3. 各专业出勤率分析
        st.subheader("3. 各专业出勤率分析")
        
        col_chart3, col_table3 = st.columns([2, 1])
        
        with col_chart3:
            st.write("各专业平均出勤率")
            # 按专业计算出勤率
            attendance = df.groupby('专业')['上课出勤率'].mean()
            st.bar_chart(attendance)
        
        with col_table3:
            st.write("出勤率排名")
            attendance_df = df.groupby('专业')['上课出勤率'].mean().sort_values(ascending=False).round(5)
            st.dataframe(attendance_df, use_container_width=True)
        
        st.divider()
        
        # 4. 大数据管理专业专项分析
        st.subheader("4. 大数据管理专业专项分析")
        
        # 筛选大数据管理专业
        bigdata_df = df[df['专业'] == '大数据管理']
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.write("平均出勤率")
            st.subheader(f"{bigdata_df['上课出勤率'].mean():.1%}")
        
        with col2:
            st.write("平均期末分数")
            st.subheader(f"{bigdata_df['期末考试分数'].mean():.1f}分")
        
        with col3:
            st.write("通过率")
            pass_rate = (bigdata_df['期末考试分数'] >= 60).mean()
            st.subheader(f"{pass_rate:.1%}")
        
        with col4:
            st.write("平均学习时长")
            st.subheader(f"{bigdata_df['每周学习时长（小时）'].mean():.1f}小时")
        
        st.write("")
        
        col_hist1, col_hist2 = st.columns(2)
        
        with col_hist1:
            st.write("大数据管理专业期末成绩分布")
            # 创建期末成绩分布柱状图
            score_bins = pd.cut(bigdata_df['期末考试分数'], bins=range(30, 105, 5))
            score_counts = score_bins.value_counts().sort_index()
            score_df = pd.DataFrame({'分数区间': score_counts.index.astype(str), '人数': score_counts.values})
            score_df = score_df.set_index('分数区间')
            st.bar_chart(score_df)
        
        with col_hist2:
            st.write("大数据管理专业作业完成率分布")
            # 使用全部学生数据，取前1000人
            homework_sorted = df['作业完成率'].sort_values().reset_index(drop=True).head(10000)
            # 转换为百分比（0-100）
            homework_percent = homework_sorted * 100
            
            # 使用 Altair 设置Y轴区间
            homework_df = pd.DataFrame({'index': range(len(homework_percent)), '作业完成率': homework_percent.values})
            chart = alt.Chart(homework_df).mark_line().encode(
                x=alt.X('index:Q', title='学生序号'),
                y=alt.Y('作业完成率:Q', title='作业完成率(%)', scale=alt.Scale(domain=[60, 80]))
            ).properties(
                height=300
            )
            st.altair_chart(chart, use_container_width=True)
        
    except FileNotFoundError:
        st.error("未找到数据文件 student_data_adjusted_rounded.csv")

elif st.session_state.current_page == '模型预测':
    st.header("🎯 期末成绩预测")
    
    # 创建两列布局
    col_left, col_right = st.columns(2)
    
    with col_left:
        # 学号输入
        st.write("学号")
        student_id = st.text_input("学号", value="12312231", label_visibility="collapsed")
        
        # 性别选择
        st.write("性别")
        gender = st.selectbox("性别", ["男", "女"], label_visibility="collapsed")
        
        # 专业选择
        st.write("专业")
        major = st.selectbox("专业", ["信息系统", "人工智能", "大数据管理", "工商管理", "电子商务", "财务管理"], label_visibility="collapsed")
    
    with col_right:
        # 每周学习时长滑块
        st.write("每周学习时长(小时)")
        study_hours = st.slider("每周学习时长", min_value=0, max_value=40, value=20, label_visibility="collapsed")
        
        # 上课出勤率滑块
        st.write("上课出勤率")
        attendance = st.slider("上课出勤率", min_value=0, max_value=100, value=100, label_visibility="collapsed")
        
        # 期中考试分数滑块
        st.write("期中考试分数")
        midterm_score = st.slider("期中考试分数", min_value=0, max_value=100, value=40, label_visibility="collapsed")
        
        # 作业完成率滑块
        st.write("作业完成率")
        homework_rate = st.slider("作业完成率", min_value=0, max_value=100, value=80, label_visibility="collapsed")
    
    st.write("")
    
    # 预测按钮
    if st.button("预测期末成绩", type="primary"):
        try:
            import pickle
            
            # 加载模型
            with open('student_model.pkl', 'rb') as f:
                model = pickle.load(f)
            
            # 准备输入数据
            input_data = pd.DataFrame({
                '性别': [gender],
                '专业': [major],
                '每周学习时长（小时）': [study_hours],
                '上课出勤率': [attendance / 100],
                '期中考试分数': [midterm_score],
                '作业完成率': [homework_rate / 100]
            })
            
            # 独热编码
            input_encoded = pd.get_dummies(input_data)
            
            # 确保特征列与训练时一致
            df_temp = pd.read_csv('student_data_adjusted_rounded.csv')
            features_temp = df_temp[['性别', '专业', '每周学习时长（小时）', '上课出勤率', '期中考试分数', '作业完成率']]
            features_temp = pd.get_dummies(features_temp)
            
            # 对齐列
            for col in features_temp.columns:
                if col not in input_encoded.columns:
                    input_encoded[col] = 0
            input_encoded = input_encoded[features_temp.columns]
            
            # 预测
            prediction = model.predict(input_encoded)[0]
            
            st.success(f"🎯 预测期末成绩: {prediction:.2f} 分")
            
            # 学习建议
            if prediction >= 90:
                st.info("📚 学习建议: 成绩优秀，继续保持！")
            elif prediction >= 80:
                st.info("📚 学习建议: 成绩良好，可以挑战更高目标！")
            elif prediction >= 60:
                st.info("📚 学习建议: 成绩及格，建议增加学习时长和出勤率。")
            else:
                st.warning("📚 学习建议: 成绩不理想，建议加强学习，提高出勤率和作业完成率。")
                
        except FileNotFoundError:
            st.error("未找到模型文件，请先运行 train_student_model.py 训练模型")

elif st.session_state.current_page == '可视化展示':
    st.header("📊 可视化展示")
    st.write("可视化展示页面内容")
