import csv
import re
import os
os.chdir('../../')

# テスト用にKEN_ALL.csvのデータの都道府県、市区町村、その他の部分を結合する
# 結合したデータを再度分割しつつ一致するか判定することで答え合わせをする
with open('data/input/220930_KEN_ALL.csv', encoding='sjis') as f:
    reader = csv.reader(f)
    data = [row for row in reader]
address_list = []
for i in range(len(data)):
    address_list += [[data[i][6] + data[i][7] + data[i][8], data[i][6], data[i][7], data[i][8]]]

# 都道府県を抽出する
pattern = '''(...??[都道府県])'''
match_count = 0
for i in range(len(data)):
    result = re.match(pattern, address_list[i][0])
    if  result.group(1) == address_list[i][1]:
        match_count += 1
    else:
        print(address_list[i][1], result.group(1))
print('データ数=', len(data),'; マッチ数=', match_count, '; アンマッチ数=', len(data)-match_count, '; マッチ率=', '{:.1%}'.format(match_count/len(data)))

pattern = '''(...??[都道府県])(.+?[市区町村])'''
match_count = 0
for i in range(len(data)):
    result = re.match(pattern, address_list[i][0])
    if result.group(2) == address_list[i][2]:
        match_count += 1
    else:
        if i % 50 == 0: # 全数だと膨大になるのでサンプリングして抽出
            print(address_list[i][1], address_list[i][2], result.group(2))
print('データ数=', len(data),'; マッチ数=', match_count, '; アンマッチ数=', len(data)-match_count, '; マッチ率=', '{:.1%}'.format(match_count/len(data)))

pattern = '''(...??[都道府県])(.+?市.+?区|.+?[市区町村])'''
match_count = 0
for i in range(len(data)):
    result = re.match(pattern, address_list[i][0])
    if result.group(2) == address_list[i][2]:
        match_count += 1
    else:
        if i % 50 == 0: # 全数だと膨大になるのでサンプリングして抽出
            print(address_list[i][1], address_list[i][2], result.group(2))
print('データ数=', len(data),'; マッチ数=', match_count, '; アンマッチ数=', len(data)-match_count, '; マッチ率=', '{:.1%}'.format(match_count/len(data)))

pattern = '''(...??[都道府県])(.+?郡.+?[町村]|.+?市.+?区|.+?[区]|.+?[市]|.+?[町村])'''
match_count = 0
for i in range(len(data)):
    result = re.match(pattern, address_list[i][0])
    if result.group(2) == address_list[i][2]:
        match_count += 1
    else:
        print(address_list[i][1], address_list[i][2], result.group(2))
print('データ数=', len(data),'; マッチ数=', match_count, '; アンマッチ数=', len(data)-match_count, '; マッチ率=', '{:.1%}'.format(match_count/len(data)))

# 政令指定都市を例外処理する方向に方針転換
pattern = '''(...??[都道府県])((?:札幌|仙台|さいたま|千葉|横浜|川崎|相模原|新潟|静岡|浜松|名古屋|京都|大阪|堺|神戸|岡山|広島|北九州|福岡|熊本)市.+?区|.+?郡.+?[町村]|.+?[市]|.+?[区町村])'''
match_count = 0
for i in range(len(data)):
    result = re.match(pattern, address_list[i][0])
    if result.group(2) == address_list[i][2]:
        match_count += 1
    else:
        print(address_list[i][1], address_list[i][2], result.group(2))
print('データ数=', len(data),'; マッチ数=', match_count, '; アンマッチ数=', len(data)-match_count, '; マッチ率=', '{:.1%}'.format(match_count/len(data)))

pattern = '''(...??[都道府県])((?:札幌|仙台|さいたま|千葉|横浜|川崎|相模原|新潟|静岡|浜松|名古屋|京都|大阪|堺|神戸|岡山|広島|北九州|福岡|熊本)市.+?区|(?:余市|高市|[^市]+?)郡(?:玉村|.+?)[町村]|[^市]+?[区]|(?:野々市|四日市|廿日市|.+?)[市]|.+?[町村])'''
match_count = 0
for i in range(len(data)):
    result = re.match(pattern, address_list[i][0])
    if result.group(2) == address_list[i][2]:
        match_count += 1
    else:
        print(address_list[i][1], address_list[i][2], result.group(2))
print('データ数=', len(data),'; マッチ数=', match_count, '; アンマッチ数=', len(data)-match_count, '; マッチ率=', '{:.1%}'.format(match_count/len(data)))

pattern = '''(...??[都道府県])((?:札幌|仙台|さいたま|千葉|横浜|川崎|相模原|新潟|静岡|浜松|名古屋|京都|大阪|堺|神戸|岡山|広島|北九州|福岡|熊本)市.+?区|(?:蒲郡|大和郡山)市|.+?郡(?:玉村|大町|.+?)[町村]|[^市]+?[区]|(?:野々市|四日市|廿日市|.+?)[市]|.+?[町村])(.+)'''
match_count = 0
for i in range(len(data)):
    result = re.match(pattern, address_list[i][0])
    if result.group(2) == address_list[i][2]:
        match_count += 1
    else:
        print(address_list[i][1], address_list[i][2], result.group(2))
print('データ数=', len(data),'; マッチ数=', match_count, '; アンマッチ数=', len(data)-match_count, '; マッチ率=', '{:.1%}'.format(match_count/len(data)))

# 結局文字数は多くなった…
print('旧=', len('(...??[都道府県])((?:旭川|伊達|石狩|盛岡|奥州|田村|南相馬|那須塩原|東村山|武蔵村山|羽村|十日町|上越|富山|野々市|大町|蒲郡|四日市|姫路|大和郡山|廿日市|下松|岩国|田川|大村)市|.+?郡(?:玉村|大町|.+?)[町村]|.+?市.+?区|.+?[市区町村])(.+)'), '; 新=', len('(...??[都道府県])((?:札幌|仙台|さいたま|千葉|横浜|川崎|相模原|新潟|静岡|浜松|名古屋|京都|大阪|堺|神戸|岡山|広島|北九州|福岡|熊本)市.+?区|(?:蒲郡|大和郡山)市|.+?郡(?:玉村|大町|.+?)[町村]|[^市]+?[区]|(?:野々市|四日市|廿日市|.+?)[市]|.+?[町村])(.+)'))