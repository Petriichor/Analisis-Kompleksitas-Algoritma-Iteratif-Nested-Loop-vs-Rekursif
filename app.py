from flask import Flask, render_template, request
import time, matplotlib, io, base64, sys, random

# Agar matplotlib tidak error di server tanpa monitor
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Set limit rekursi agar aman untuk pengujian n besar
sys.setrecursionlimit(20000)

app = Flask(__name__)

# Algoritma Iteratif (Nested Loop)
def bubble_iterative(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Algoritma Rekursif
def bubble_recursive(arr, n=None):
    if n is None: n = len(arr)
    if n <= 1: return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    bubble_recursive(arr, n - 1)

def generate_plot():
    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    n_target = int(request.form.get('n_target', 100))
    step = max(1, n_target // 12)
    sizes = list(range(1, n_target + 1, step))
    if n_target not in sizes: sizes.append(n_target)
    
    t_iter_list, t_recur_list = [], []
    single_res = {}

    for n in sizes:
        data_awal = [random.randint(1, 1000) for _ in range(n)]
        
        # Hitung Iteratif
        d_it = data_awal.copy()
        start = time.perf_counter()
        bubble_iterative(d_it)
        ti = time.perf_counter() - start
        
        # Hitung Rekursif (Batasi n=5000)
        tr = None
        if n <= 5000:
            d_rec = data_awal.copy()
            try:
                start = time.perf_counter()
                bubble_recursive(d_rec)
                tr = time.perf_counter() - start
            except: tr = None
        
        t_iter_list.append(ti)
        t_recur_list.append(tr)
        
        if n == n_target:
            diff = abs(tr - ti) if tr is not None else None
            single_res = {'n': n, 't_iter': ti, 't_recur': tr, 'diff': diff}

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, t_iter_list, 'b-o', label='Iteratif')
    r_valid = [i for i, v in enumerate(t_recur_list) if v is not None]
    if r_valid:
        plt.plot([sizes[i] for i in r_valid], [t_recur_list[i] for i in r_valid], 'r-s', label='Rekursif')
    plt.title(f'Grafik Perbandingan Running Time (n=1 sampai {n_target})')
    plt.xlabel('n'); plt.ylabel('Detik'); plt.legend(); plt.grid(True)
    plot_comp = generate_plot()

    return render_template('index.html', single_result=single_res, plot_comp=plot_comp)

if __name__ == '__main__':
    app.run(debug=True)