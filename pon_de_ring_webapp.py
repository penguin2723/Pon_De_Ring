from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image



st.title('ポン・デ・リング方程式')

st.write('導出等は下記のリンクから元動画をご覧ください．')

link = '[ポンデリングをグラフで描いてみる](https://www.nicovideo.jp/watch/sm34091710)'
st.markdown(link, unsafe_allow_html=True)

st.write(r'''
	媒介変数$\theta$と$\phi$を用いて，ポン・デ・リング方程式は$xyz$空間上に下記のように表せる.
	''')

st.write(r'''
	$f(\theta) = \theta - \frac{\pi}{4}\lfloor \frac{4}{\pi}(\theta + \frac{\pi}{8}) \rfloor \hspace{2mm}$とすると,
	''')

st.latex(r'''
	x = \left(a \cos{f(\theta)} + \cos{\phi} \sqrt{b^2 - a^2 \sin^2{f(\theta)}}\right)\cos{\theta}
	''')
st.latex(r'''
	y = \left(a \cos{f(\theta)} + \cos{\phi} \sqrt{b^2 - a^2 \sin^2{f(\theta)}}\right)\sin{\theta}
	''')
st.latex(r'''
	z = \sin{\phi} \sqrt{b^2 - a^2 \sin^2{f(\theta)}}
	''')

st.write(r'''
	各変数，定数の条件は次の様になる.$\quad$
	$0 < \theta,\hspace{2mm}$ $\phi < 2\pi,\hspace{2mm}$ $a,b \in \mathrm{R} > 0,\hspace{2mm}$ $\sin{\frac{\pi}{8} < \frac{b}{a}}.$
	''')

_theta = np.linspace(0, 2*np.pi, 100)
_phi = np.linspace(0, 2*np.pi, 100)

func_theta = list()
for i in _theta:
    i = i - np.pi/4 * np.floor(4/np.pi * (i + np.pi/8))
    func_theta.append(i)
func_theta = np.array(func_theta)


df_1 = pd.DataFrame({
    'θ': _theta,
    'φ': _phi,
    'f(θ)': func_theta,
})

st.write(r'''
	計算の都合上$\hspace{2mm}\theta < 2\pi \hspace{2mm}$とし，今回は$\hspace{2mm}\theta, \hspace{1mm}\phi \hspace{2mm}$を百等分します．
	''')

st.dataframe(df_1.style.highlight_max(axis=0))

_theta_mesh, _phi_mesh = np.meshgrid(_theta, _phi)

func_theta_mesh = list()
for i in _theta_mesh:
    i = i - np.pi/4 * np.floor(4/np.pi * (i + np.pi/8))
    func_theta_mesh.append(i)
func_theta_mesh = np.array(func_theta_mesh)

df_2 = pd.DataFrame({
    'θ_mesh': _theta_mesh[0],
    'φ_mesh': _phi_mesh[0],
    'f(θ)_mesh': func_theta_mesh[0],
})

df_3 = pd.DataFrame({
    'θ_mesh': _theta_mesh[1],
    'φ_mesh': _phi_mesh[1],
    'f(θ)_mesh': func_theta_mesh[1],
})

st.write(r'''
	さらに，$\hspace{2mm}\theta,\hspace{1mm}\phi\hspace{2mm}$をメッシュ化します．$\hspace{2mm}f(\theta)\hspace{2mm}$は$\hspace{2mm}\theta\hspace{2mm}$から計算されるので自動的にその値を得ます．
	''')
	
st.write(r'''
	下の表は要素の一番目だけを表示しています．百等分をさらに百等分して一万個に分けられています．
	''')

st.dataframe(df_2.style.highlight_max(axis=0))
st.dataframe(df_3.style.highlight_max(axis=0))

st.write(r'''
	上の三つの表からわかるように$\hspace{2mm}f(\theta)\hspace{2mm}$は$\hspace{2mm}\theta\hspace{2mm}$と同じ規則でメッシュ化されていて，$\hspace{2mm}\phi\hspace{2mm}$はその通りではありません．
	''')

a = 9
b = 4

x = (a * np.cos(func_theta_mesh) + np.cos(_phi_mesh) * np.sqrt(b**2 - a**2 * np.sin(func_theta_mesh)**2)) * np.cos(_theta_mesh)
y = (a * np.cos(func_theta_mesh) + np.cos(_phi_mesh) * np.sqrt(b**2 - a**2 * np.sin(func_theta_mesh)**2)) * np.sin(_theta_mesh)
z = np.sin(_phi_mesh) * np.sqrt(b**2 - a**2 * np.sin(func_theta_mesh)**2)

st.write(r'''
	今回は$\hspace{2mm}a = 9,\hspace{1mm}b = 4\hspace{2mm}$とします．メッシュ化された値とともに方程式に代入し，プロットすればポン・デ・リングの完成です．
	''')


fig = plt.figure() 
ax = Axes3D(fig) 
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
ax.set_zlim(-10,10)
ax.plot_surface(x, y, z, color = st.color_picker('美味しそうな色は？', '#afeeee')) 
plt.axis('off')

st.pyplot(fig)

image = Image.open('images/pon_de_ring.jpg')
st.image(image, caption='ポンデリング')

degrees = st.radio(
	'腹何分目？',
	('満腹', '八分目', '六分目', '四分目', '二分目', '食指が動かなかった'),
	5
	)
	
i = 0

if degrees == '満腹':
	while i < 5:
		st.balloons()
		i += 1
elif degrees == '八分目':
	while i < 4:
		st.balloons()
		i += 1
elif degrees == '六分目':
	while i < 3:
		st.balloons()
		i += 1
elif degrees == '四分目':
	while i < 2:
		st.balloons()
		i += 1
elif degrees == '二分目':
	st.balloons()
else:
    st.write('Reaaaally?')	
	
	
