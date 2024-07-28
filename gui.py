import tkinter as tk
from tkinter import ttk
import database

def atualizar_lista():
    conn = database.conectar()
    registros = database.buscar_dados(conn, entry_pesquisa.get())
    conn.close()
    for i in tree.get_children():
        tree.delete(i)
    for registro in registros:
        tree.insert('', 'end', values=registro)

def on_inserir():
    num_situacao = entry_num_situacao.get()
    num_cx = entry_num_cx.get()
    data = entry_data.get()
    descricao = entry_descricao.get()
    if num_situacao and num_cx and data and descricao:
        conn = database.conectar()
        database.inserir_dados(conn, num_situacao, num_cx, data, descricao)
        conn.close()
        atualizar_lista()
        entry_num_situacao.delete(0, tk.END)
        entry_num_cx.delete(0, tk.END)
        entry_data.delete(0, tk.END)
        entry_descricao.delete(0, tk.END)
    else:
        label_status.config(text="Todos os campos são obrigatórios!", fg="red")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerenciamento de Caixa com Problemas")
root.geometry("1000x600")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Configuração de fonte para labels, entradas e botões
font_label = ('Arial', 12)
font_entry = ('Arial', 12)
font_button = ('Arial', 12, 'bold')

# Labels e Entries para entrada de dados
label_num_situacao = tk.Label(frame, text="Número da Situação:", font=font_label)
label_num_situacao.grid(row=0, column=0, padx=5, pady=5, sticky='w')
entry_num_situacao = tk.Entry(frame, font=font_entry)
entry_num_situacao.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

label_num_cx = tk.Label(frame, text="Número da Caixa:", font=font_label)
label_num_cx.grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_num_cx = tk.Entry(frame, font=font_entry)
entry_num_cx.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

label_data = tk.Label(frame, text="Data:", font=font_label)
label_data.grid(row=2, column=0, padx=5, pady=5, sticky='w')
entry_data = tk.Entry(frame, font=font_entry)
entry_data.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

label_descricao = tk.Label(frame, text="Descrição:", font=font_label)
label_descricao.grid(row=3, column=0, padx=5, pady=5, sticky='w')
entry_descricao = tk.Entry(frame, font=font_entry)
entry_descricao.grid(row=3, column=1, padx=5, pady=5, sticky='ew')

# Botão para inserir dados
button_inserir = tk.Button(frame, text="Inserir", command=on_inserir, font=font_button)
button_inserir.grid(row=4, columnspan=2, pady=10)

label_status = tk.Label(frame, text="", font=font_label)
label_status.grid(row=5, columnspan=2, pady=5)

# Barra de pesquisa
label_pesquisa = tk.Label(frame, text="Pesquisar:", font=font_label)
label_pesquisa.grid(row=6, column=0, padx=5, pady=5, sticky='w')
entry_pesquisa = tk.Entry(frame, font=font_entry)
entry_pesquisa.grid(row=6, column=1, padx=5, pady=5, sticky='ew')
button_pesquisar = tk.Button(frame, text="Pesquisar", command=atualizar_lista, font=font_button)
button_pesquisar.grid(row=7, columnspan=2, pady=10)

# Treeview para exibir os dados do banco de dados
tree = ttk.Treeview(root, columns=("num_situacao", "num_cx", "data", "descricao"), show='headings')
tree.heading("num_situacao", text="Número da Situação")
tree.heading("num_cx", text="Número da Caixa")
tree.heading("data", text="Data")
tree.heading("descricao", text="Descrição")
tree.column("num_situacao", width=100, anchor='w')
tree.column("num_cx", width=150, anchor='w')
tree.column("data", width=100, anchor='w')
tree.column("descricao", width=300, anchor='w')
tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Inicializa o banco de dados e atualiza a lista de dados
conn = database.conectar()
database.criar_tabela(conn)
conn.close()
atualizar_lista()

root.mainloop()
