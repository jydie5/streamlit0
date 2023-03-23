import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('おじの最初のデプロイ')
st.write('プログレスバー')

'Start!'

latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.02)
'Done!'



st.write('インタラクティブなテキスト')

left_column,right_column=st.columns(2)
button=left_column.button('右カラムに文字を表示')
if left_column.button:
    right_column.write('ボタンが押されました')


expander=st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text=st.sidebar.text_input('あなたの趣味を教えてください')
# 'あなたのしゅみは',text

# condi=st.sidebar.slider('あなたの調子は？',0,100,50)
# 'そうですか',condi






# text=st.text_input('あなたの趣味を教えてください')
# 'あなたのしゅみは',text,'です'

# condi=st.slider('あなたの調子は？',0,100,50)
# 'そうですか',condi,'ですね'

# st.write('Display Image')

# options=st.selectbox('好きな数字は？',list(range(1,11)))
# 'あなたの好きな数字は',options,'ですね'

if st.checkbox('show image'):
    img=Image.open('sample.jpg')
    st.image(img,caption='tank custam',use_column_width=True)


#st.line_chart(df)




#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0),width=100,height=100)
#st.table(df.style.highlight_max(axis=0))


df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']

)

st.map(df)


"""

# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```






"""