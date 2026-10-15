import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib
import os
import shutil
from datetime import datetime

class MD5ModifierApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('视频MD5修改工具')
        
        # 文件选择区域
        self.file_frame = tk.Frame(self.root)
        self.file_path = tk.StringVar()
        tk.Label(self.file_frame, text='视频文件:').pack(side='left')
        tk.Entry(self.file_frame, textvariable=self.file_path, width=40).pack(side='left')
        tk.Button(self.file_frame, text='选择文件', command=self.select_file).pack(side='left')
        self.file_frame.pack(pady=10)

        # MD5显示区域
        self.md5_frame = tk.Frame(self.root)
        tk.Label(self.md5_frame, text='原始MD5:').pack(side='left')
        self.original_md5 = tk.Label(self.md5_frame, text='')
        self.original_md5.pack(side='left')
        self.md5_frame.pack(pady=5)

        # 操作按钮
        self.modify_btn = tk.Button(self.root, text='修改MD5', command=self.modify_md5, state='disabled')
        self.modify_btn.pack(pady=5)
        
        # 新MD5显示
        self.new_md5_frame = tk.Frame(self.root)
        tk.Label(self.new_md5_frame, text='新MD5:').pack(side='left')
        self.new_md5 = tk.Label(self.new_md5_frame, text='')
        self.new_md5.pack(side='left')
        self.new_md5_frame.pack(pady=5)

        # 保存按钮
        self.save_btn = tk.Button(self.root, text='保存文件', command=self.save_file, state='disabled')
        self.save_btn.pack(pady=10)

        self.temp_file = None

    def select_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[('视频文件', '*.mp4 *.avi *.mov *.mkv')]
        )
        if file_path:
            self.file_path.set(file_path)
            self.calculate_original_md5(file_path)
            self.modify_btn.config(state='normal')

    def calculate_original_md5(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5()
                while chunk := f.read(8192):
                    file_hash.update(chunk)
            self.original_md5.config(text=file_hash.hexdigest())
        except Exception as e:
            messagebox.showerror('错误', f'读取文件失败: {str(e)}')

    def modify_md5(self):
        try:
            # 创建临时文件
            self.temp_file = self.file_path.get() + '.tmp'
            shutil.copyfile(self.file_path.get(), self.temp_file)
            
            # 追加时间戳修改MD5
            with open(self.temp_file, 'ab') as f:
                f.write(str(datetime.now().timestamp()).encode())
            
            # 计算新MD5
            with open(self.temp_file, 'rb') as f:
                file_hash = hashlib.md5()
                while chunk := f.read(8192):
                    file_hash.update(chunk)
            self.new_md5.config(text=file_hash.hexdigest())
            self.save_btn.config(state='normal')
            messagebox.showinfo('成功', 'MD5修改完成！')
        except Exception as e:
            messagebox.showerror('错误', f'修改失败: {str(e)}')

    def save_file(self):
        save_path = filedialog.asksaveasfilename(
            defaultextension='.mp4',
            filetypes=[('MP4视频', '*.mp4'), ('AVI视频', '*.avi'), ('所有文件', '*.*')]
        )
        if save_path:
            try:
                shutil.move(self.temp_file, save_path)
                messagebox.showinfo('成功', f'文件已保存到:\n{save_path}')
                self.reset_ui()
            except Exception as e:
                messagebox.showerror('错误', f'保存失败: {str(e)}')

    def reset_ui(self):
        self.file_path.set('')
        self.original_md5.config(text='')
        self.new_md5.config(text='')
        self.modify_btn.config(state='disabled')
        self.save_btn.config(state='disabled')
        self.temp_file = None

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = MD5ModifierApp()
    app.run()