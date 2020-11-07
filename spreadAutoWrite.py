import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials

JSONF = "----------------------.json"
SPREAD_SHEET_KEY = "------------------------------"

def connect_gspread():
    #spreadsheetsとdriveの2つのAPIを指定する
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    #認証情報を設定する
    credentials = ServiceAccountCredentials.from_json_keyfile_name(JSONF, scope)
    gc = gspread.authorize(credentials)
    #スプレッドシートキーを用いて、sheet1にアクセスする
    worksheet = gc.open_by_key(SPREAD_SHEET_KEY).sheet1
    return worksheet

def main():
    # jsonファイル(秘密鍵)と対象のspreadSheetを取得
    ws = connect_gspread()
    #sheetの値を取得
    cellInfo = ws.range('A1:A30')
    #for文の書き方例１
    for row in range(len(cellInfo)):
        pass
    #for文の書き方例２
    for cell in cellInfo:
        if not cell.value:
            ws.update_cell(cell.row, cell.col+1,"空文字")
            ws.format(cell.address, {
                "backgroundColor": {
                    "red": 0.0,
                    "green": 1.0,
                    "blue": 1.0
                },
                "textFormat": {
                    "foregroundColor": {
                        "red": 1.0,
                        "green": 0.0,
                        "blue": 0.0
                    },
                }
            })
        else:
            ws.update_cell(cell.row, cell.col+1,"ウェイ")
    #(２−１)あるセルの値を更新（行と列を指定）
    #ws.update_cell(1,1,"test1")
    #ws.update_cell(2,1,1)
    #ws.update_cell(3,1,2)
    #(２−２)あるセルの値を更新（ラベルを指定）
    ws.update_acell('C1','test2')
    ws.update_acell('C2',1)
    ws.update_acell('C3',2)
    #(2-3)ある範囲のセルの値を更新
    ds = ws.range('E1:G3')
    print(ds)
    ds[0].value = 1
    ds[1].value = 2
    ds[2].value = 3
    ds[3].value = 4
    ds[4].value = 5
    ds[5].value = 6
    ds[6].value = 7
    ds[7].value = 8
    ds[8].value = 9
    ws.update_cells(ds)
    ws.format("C1:C3", {
        "backgroundColor": {
            "red": 0.0,
            "green": 0.0,
            "blue": 0.0
        },
        "horizontalAlignment": "CENTER",
        "textFormat": {
            "foregroundColor": {
                "red": 1.0,
                "green": 1.0,
                "blue": 1.0
            },
            "fontSize": 12,
        }
    })

    cell = ws.cell(1, 1)
    cellAddress = cell.address
    print(cellAddress)

if __name__ == "__main__":
    main()
