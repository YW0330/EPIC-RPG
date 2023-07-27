# EPIC RPG
此專案支援 Discord Bot **EPIC RPG** 的快速傳輸命令。
## 準備項目
- 安裝 Chrome 瀏覽器
  - 需要是中文介面
- 安裝 Python
  - Python version: Python 3.10.7
## 個人化設定
### 文字文件
- `infomation.txt`
  - `URL`: 填寫帳號的 Discord 網址
  - `CHANNEL`: 填寫 EPIC RPG 之頻道名稱，需要包含 `#` 字號
  - `ACCOUNT`: 填寫 `email` 
  - `PASSWORD`: 填寫 `密碼`
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
- Ubuntu 16.04 下測試成功