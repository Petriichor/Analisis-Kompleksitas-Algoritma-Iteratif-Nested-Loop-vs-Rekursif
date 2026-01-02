from flask import Flask, render_template, request
import time, matplotlib, io, base64, sys

matplotlib.use('Agg')
import matplotlib.pyplot as plt
sys.setrecursionlimit(1000000)

app = Flask(__name__)

# --- ALGORITMA ITERATIF (PARABOLA) ---
def aritmatika_iterative(n):
    total = 0
    for i in range(1, n + 1):
        for _ in range(i):
            total += 1 
    return total

# --- 2. ALGORITMA REKURSIF (LINEAR) ---
def aritmatika_recursive(n):
    if n <= 0:
        return 0
    return n + aritmatika_recursive(n - 1)

def get_base64_plot():
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
    try:
        n_target = int(request.form.get('n_target', 100))
    except ValueError:
        n_target = 100

    step = max(1, n_target // 10)
    sizes = list(range(1, n_target + 1, step))
    if n_target not in sizes:
        sizes.append(n_target)

    t_iter_list = []
    t_recur_list = []
    single_res = {}

    for n in sizes:
        start = time.perf_counter()
        res_iter = aritmatika_iterative(n)
        ti = time.perf_counter() - start
        t_iter_list.append(ti)

        tr = None
        try:
            start = time.perf_counter()
            res_recur = aritmatika_recursive(n)
            tr = time.perf_counter() - start
        except RecursionError:
            tr = None
        
        t_recur_list.append(tr)

        if n == n_target:
            diff = abs(tr - ti) if tr is not None else 0
            single_res = {
                'n': n,
                't_iter': ti,
                't_recur': tr,
                'diff': diff,
                'result': res_iter 
            }

    # --- GENERATE GRAFIK ---
    
    # 1. Grafik Perbandingan (Iteratif vs Rekursif)
    plt.figure(figsize=(10, 5))
    plt.plot(sizes, t_iter_list, 'b-o', label='Iteratif (Nested Loop - O(n^2))')
    
    valid_r_idx = [i for i, val in enumerate(t_recur_list) if val is not None]
    if valid_r_idx:
        valid_sizes = [sizes[i] for i in valid_r_idx]
        valid_times = [t_recur_list[i] for i in valid_r_idx]
        plt.plot(valid_sizes, valid_times, 'r-s', label='Rekursif (Linear - O(n))')

    plt.title(f'Perbandingan Waktu Eksekusi (n=1 s.d {n_target})')
    plt.xlabel('Input Size (n)')
    plt.ylabel('Waktu (detik)')
    plt.legend()
    plt.grid(True)
    plot_comp = get_base64_plot()

    # 2. Grafik Iteratif Saja (Untuk melihat lengkungan Parabola)
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, t_iter_list, 'b-o')
    plt.title('Iteratif: Nested Loop (Kuadratik)')
    plt.xlabel('n'); plt.ylabel('Detik'); plt.grid(True)
    plot_iter = get_base64_plot()

    # 3. Grafik Rekursif Saja (Untuk melihat garis Linear)
    plt.figure(figsize=(8, 5))
    if valid_r_idx:
        plt.plot(valid_sizes, valid_times, 'r-s', color='red')
    plt.title('Rekursif: Linear')
    plt.xlabel('n'); plt.ylabel('Detik'); plt.grid(True)
    plot_recur = get_base64_plot()

    return render_template('index.html', 
                           single_result=single_res, 
                           plot_comp=plot_comp,
                           plot_iter=plot_iter,
                           plot_recur=plot_recur)

if __name__ == '__main__':
    app.run(debug=True)
