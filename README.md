# EPIC RPG
此專案支援 Discord Bot **EPIC RPG** 的快速傳輸命令。
## 準備項目
- 安裝 Chrome 瀏覽器
  - 需要是中文介面
- 安裝 Python
  - Python version: Python 3.9
## 個人化設定
### Discord 相關
- `rpg/util.py`
  - `URL` 填寫自己的 Discord 網址
  - `CHANNEL` 填寫自己的頻道名稱，需要包含`#`字號
### 文字文件
- `password.txt`
  - 第一行填 `email` 
  - 第二行填 `password`
- `commandSet.txt`
  - 依照想要的顯示順序填寫 EPIC RPG 命令
## 原始碼操作方式
### 安裝相關模組
```shell
pip install -r requirement.txt
```
### 執行程式
```shell
python -m rpg
```
### Pyinstaller 打包成可執行檔
```shell
python scripts/build_exec.py 
```
## 備註
- 執行打包後程式若出現console視窗，需要到 `C:\Users\USER\AppData\Local\Programs\Python\Python39\Lib\site-packages\selenium\webdriver\common\service.py` 進行修改
    ```diff=47
    - self.creationflags = 0
    + self.creationflags = 0x08000000
    ```
- Ubuntu 16.04 下測試成功