import time
import random

Player = input("請輸入你的姓名（三個字）：")

#序章
Part1_begin = "前情提要"
print(f"\n{Part1_begin:*^24s}")
print(f"{Player}在午休結束與梅川伊芙道別後（詳情見期初專案）")
print("由於不想上課便前往東側門對面的超商8-TWELVE買東西")
time.sleep(1)
Item_1 = input("\n「你好歡迎光臨，請問需要什麼嗎？」（任意填寫）：")
print(f"「謝謝您的惠顧。」{Player[1:]}買完便走出店外，痴痴地看著漫長的紅燈")
time.sleep(1)
print(f"或許是因為沒睡午覺而感到疲倦，{Player[1:]}下意識地揉了眼睛……")
for i in range(5, 0, -1):
    for j in range(i):
        print(".", end="")
    print()
    time.sleep(0.5)

#主軸
Start = True                         #開局用
Dead = False                         #死亡狀態
n = 0                                #死亡次數
Fruit = False                        #榴槤(打王加成)
Heroine = False                      #觸發女主事件
Item_2 = ["立體驅動裝置",False]      #擋死道具1
Item_3 = ["二天一流秘笈",False]      #擋死道具2
Item_4 = ["劍鞘阿瓦隆",False]        #擋死道具3
Item_5 = ["希波呂忒的腰帶",False]    #探索道具1
Item_6 = ["聖園的金蘋果",False]      #探索道具2
Item_7 = ["西片同學的橡皮擦",False]  #真結局條件1
Item_8 = ["B小町的專輯",False]       #真結局條件2

while Start == True or Dead == True:
    Start = False
    Dead = False
    Heroine = False
    Item_2[1] = False
    Item_3[1] = False
    Item_4[1] = False
    Item_5[1] = False
    Item_6[1] = False
    Item_7[1] = False
    Item_8[1] = False
    print("\n「小哥，買榴槤嗎？」\n") #重生起點
    time.sleep(1)
    print(Player[1:] + "再度睜開雙眼，映入眼簾的是向自己搭話的水果攤大叔")
    time.sleep(1)
    if n == 0: #依照死亡次數觸發不同劇情
        print("周遭人群的奇裝異服、在街道上來往的馬車，眼前光景過於陌生使腦袋頓時一片空白")
        time.sleep(1)
        print(f"\n「我這是穿越到異世界了嗎？」{Player[1:]}整理完思緒後這麼說著")
        time.sleep(1)
        print("\n「按照多年來豐富的遊戲經驗，首先肯定是去武器店買一把斷鋼聖劍，")
        print("打倒魔王後返回王都，並四處打聽回到原本世界的方法。」")
        print(f"構思著未來美好藍圖的{Player[1:]}，邁出了他在異世界的第一步")
        time.sleep(1)
    elif n == 1:
        print("\n「什麼？」")
        time.sleep(2)
        print("\n「在問你呢！要不要買顆榴槤？」大叔又再一次問道")
        time.sleep(1)
        print("\n看著眼前似曾相似的光景，我不禁捏了一下臉頰確認是不是在作夢")
        print("感受著臉頰的痛楚，儘管心中仍有一絲疑惑，還是先按原計畫前往武器店吧")
        time.sleep(1)
    elif n == 2:
        print(f"眼前的景象實在過於詫異，{Player[1:]}當場原地昏倒了")
        time.sleep(2)
        print(f"\n過了一段時間後{Player[1:]}再次醒來，才接受了自己「死亡輪迴」的事實與能力")
        time.sleep(1)
        print("\n「看你臉色很糟的樣子，這顆榴槤你就先收下吧」")
        Fruit = True #死兩次拿到榴槤
        print("從大叔手中接過榴槤後，便往武器店的方向走去")
        time.sleep(1)
    else: #死三次之後劇情固定
        print("\n逐漸適應了死亡回歸")
        print(f"這一次{Player[1:]}沒有猶豫，轉身便前往武器店")
        time.sleep(1)
    print("\n武器店似乎在街廓的另一側，要怎麼走呢？") #前往武器店
    Choice_1 = input("1.沿著大街  2.捷徑的小巷子  ：")
    if Choice_1 == "1":
        print("路上人車壅塞，比預期多花了點時間才抵達目的地")
        time.sleep(1)
    elif Choice_1 == "2": #走巷子觸發事件
        print("走在昏暗的巷子裡，面前突然有三個身影擋住去路")
        time.sleep(1)
        print("\n「不想死的話就把錢交出來！」三個8+9踏著六親不認的步伐逼近")
        print("其中一人亮出手中的小刀，是否要和他們戰鬥？")
        Choice_11 = input("1.戰鬥  2.逃跑  ：")
        if Choice_11 == "1":
            Heroine = True #觸發女主事件
            print(f"正當{Player[1:]}深吸一口氣，準備好決一死鬥……")
            time.sleep(1)
            print("\n「Explosion!」隨著少女的詠唱，一發爆裂魔法將三個8+9通通炸飛")
            time.sleep(1)
            print(f"\n「非常感謝你的出手相救，我的名字是{Player}。」我連忙回頭向少女道謝")
            print("「不會，我叫愛咪莉雅，正為了尋找過去的記憶而踏上旅途中」")
            time.sleep(1)
            print("\n「如果不嫌棄的話就讓我幫忙作為回報吧，我也在前往討伐魔王的路上」")
            print(f"「真的可以嗎？太感謝你了，那就請多指教囉！{Player[1:]}君」")
            time.sleep(1)
            print(f"\n初次相遇的愛咪莉雅和{Player[1:]}便組隊行動，兩人有說有笑地前往武器店")
            time.sleep(1)
        elif Choice_11 == "2":
            print("\n「你以為你跑得掉嗎？」8+9擺好架式，扔出手中的小刀")
            print(f"小刀以大谷翔平球速般的高速命中頭部，{Player[1:]}當場被擊倒")
            print(f"{Player[1:]}接受自己的命運，緩緩地閉上了雙眼......\n")
            time.sleep(3)
            n += 1
            Dead = True
            continue
        else:
            print(f"\n在猶豫的瞬間小刀刺中腹部，{Player[1:]}因失血過多而倒地")
            print("猶如警示著你不要亂選答案般的一道神罰")
            print(f"{Player[1:]}接受自己的命運，緩緩地閉上了雙眼……\n")
            time.sleep(3)
            n += 1
            Dead = True
            continue
    else:
        print("\n在思考的同時一輛馬車忽然失控衝向了你，當場將你輾斃")
        print("猶如警示著你不要亂選答案般的一道神罰")
        print(f"{Player[1:]}接受自己的命運，緩緩地閉上了雙眼……\n")
        time.sleep(3)
        n += 1
        Dead = True
        continue
    print(f"\n抵達武器店後，{Player[1:]}把不久前在超商買的{Item_1}拿出來跟老闆換錢") #在武器店買武器
    Coin = len(Item_1)
    print(f"「這個{Item_1}才值 {Coin} 枚金幣而已，什麼都買不起」老闆看完後如此說著")
    time.sleep(1)
    Buy = random.choice([Item_2[0],Item_3[0],Item_4[0]]) #用random抽抽
    if Buy == "立體驅動裝置":
        Item_2[1] = True
    elif Buy == "二天一流秘笈":
        Item_3[1] = True
    elif Buy == "劍鞘阿瓦隆":
        Item_4[1] = True
    else:
        pass
    print(f"\n「但我看你骨骼驚奇，是百年難得一見的練武奇才，就送你個『{Buy}』好了」")
    print(f"語畢，老闆隨手從櫃檯底下拿出{Buy}給{Player[1:]}，接著向老闆道謝後便離開前往城門")
    time.sleep(2)
    print("\n正午時分，來到了彷彿將城鎮與世界隔絕的高牆——瑪利亞之牆。") #前往城門
    time.sleep(1)
    print("\n從這裡出去的話，便將與短暫虛假的和平告別，去打倒危害世界的大魔王")
    print("但正門這裡排隊居民滿多的，是否從遠一點的側門出去呢？")
    Choice_2 = input("1.從正門出去  2.繞遠路走側門  ：")
    if Choice_2 == "1": #走正門觸發事件
        print("\n那一天，人類又回想起被巨人支配的恐懼。")
        time.sleep(1)
        print("\n在高牆之上有一對雙眸正凝視著城鎮，隨即城牆的正門處被超大型巨人踢出了一個大洞")
        if Item_2[1] == False and Heroine == False:
            print("瞬間的衝擊波摧毀了附近民房，一顆巨石也不偏不倚地砸中你，當場將你擊斃")
            print(f"{Player[1:]}接受自己的命運，緩緩地閉上了雙眼……\n")
            time.sleep(3)
            n += 1
            Dead = True
            continue
        else:
            if Item_2[1] == True: #有道具優先擋死
                print(f"瞬間的衝擊波摧毀了附近民房，千鈞一髮之際你使用了{Item_2[0]}逃開")
                print("毫髮無傷地飛上高牆，卻發現超大型巨人竟然消失了")
                print("雖然事發突然且意義不明，但總之是逃過一劫，順利離開城鎮")
                time.sleep(2)
            else:
                Heroine = False #無道具女主擋死
                print("瞬間的衝擊波摧毀了附近民房，一顆巨石朝你飛了過來")
                time.sleep(1)
                print("\n「小心！」愛咪莉雅奮力把你推向一旁，取而代之的是自己被巨石砸中")
                time.sleep(1)
                print(f"\n「雖然相處時間不長，謝謝你出現在我的人生裡……{Player[1:]}君」")
                print("奄奄一息的愛咪莉雅說完閉上了雙眼")
                print(f"一場意外導致兩人永別，而巨人也如曇花一現般消失了，{Player[1:]}只好重整心情繼續前行")
                time.sleep(2)
    elif Choice_2 == "2":
        print("雖然花了點時間，但還是順利離開城鎮了")
        time.sleep(1)
        if Heroine == True: #有女主的額外劇情
            print(f"\n過程中{Player[1:]}和愛咪莉雅望著附近如浪花拍打般搖曳的蘆葦")
            print("從興趣嗜好到理想對象，兩人相談甚歡，沉浸在只有彼此的世界裡")
            print(f"「能與你相遇真是太好了，{Player[1:]}君」說完愛咪莉雅將手放在胸前，感受心中的鼓動……")
            time.sleep(2)
        else:
            pass
    else:
        print("\n在猶豫的同時一道落雷不偏不倚地擊中你，原地應聲倒下")
        print("猶如警示著你不要亂選答案般的一道神罰")
        print(f"{Player[1:]}接受自己的命運，緩緩地閉上了雙眼……\n")
        time.sleep(3)
        n += 1
        Dead = True
        continue
    #進入第二階段
    Ex_1 = False #設定只能去一次
    Ex_2 = False 
    while Dead == False:
        print("\n接下來要前往哪裡呢？")
        Choice_3 = input("1.巖流島  2.卡美洛  3.奧林帕斯  ：")
        if Choice_3 == "1": #巖流島
            if Ex_1 == False:
                print("划著小船過了十幾分鐘終於快著陸了，但寶物好像在島的另一端")
                time.sleep(1)
                print("\n雖然整個島看起來不大，總感覺裡面有一股殺氣傳來……要怎麼走呢？")
                Choice_4 = input("1.沿著外緣繞  2.從中間穿越  ：")
                if Choice_4 == "1":
                    print("曝曬在毒辣的烈日底下，踏出的每一步都十分煎熬")
                    print(f"但為了迴避不必要的風險，{Player[1:]}堅定他的選擇繼續前行……")
                    time.sleep(2)
                elif Choice_4 == "2": #走中間觸發事件
                    print(f"上岸後{Player[1:]}筆直地前進，途中卻發現有人已在正中央的平台處等候多時")
                    print("「竟然敢遲到，那就做好覺悟吧！」說完佐佐木小次郎便舉起三尺餘太刀")
                    time.sleep(1)
                    print("\n「秘劍．燕返！」")
                    time.sleep(1)
                    if Item_3[1] == False and Heroine == False:
                        print(f"\n三個來自不同方向的斬擊同一時間迎面襲來，足以扭曲次元般的劍技使{Player[1:]}瞬間倒地")
                        print(f"{Player[1:]}接受自己的命運，緩緩地閉上了雙眼……\n")
                        time.sleep(3)
                        n += 1
                        Dead = True
                        continue
                    else:
                        if Item_3[1] == True: #有道具優先擋死
                            print(f"\n三個來自不同方向的斬擊同一時間迎面襲來，然而{Player[1:]}卻閉上了雙眼")
                            print(f"下一個瞬間{Player[1:]}手中浮現一長一短的太刀，化解了此足以扭曲次元般的劍技")
                            time.sleep(1)
                            print(f"{Player[1:]}領悟先前拿到的{Item_3[0]}，行雲流水的劍舞向佐佐木小次郎斬去")
                            time.sleep(1)
                            print(f"\n在一番交手後，活著離開此處的只有從二天一流昇華至無空境界的{Player[1:]}……")
                            time.sleep(2)
                        else:
                            Heroine = False #無道具女主擋死
                            print("\n三個來自不同方向的斬擊同一時間迎面襲來")
                            time.sleep(1)
                            print(f"\n「Explosion!」站到{Player[1:]}面前的是愛咪莉雅，隨著她的詠唱小次郎被爆裂魔法炸得體無完膚")
                            print("然而愛咪莉雅也被利刃劃出三道大傷口，兩人同一時間雙雙倒下")
                            time.sleep(1)
                            print(f"\n「雖然相處時間不長，謝謝你出現在我的人生裡...{Player[1:]}君」")
                            print("奄奄一息的愛咪莉雅說完閉上了雙眼")
                            print(f"在安葬好愛咪莉雅後，{Player[1:]}帶著她的意念邁出沉重的步伐……")
                            time.sleep(2)
                else:
                    print("上岸前頓時風雲變色，海中形成一個半徑五百公尺的大漩渦")
                    time.sleep(1)
                    print("\n隨之而來的是深海巨獸克拉肯的現身，觸手一揮便將你擊沉，落入暗黑的深淵")
                    print("猶如警示著你不要亂選答案般的一道神罰")
                    print(f"{Player[1:]}接受自己的命運，緩緩地閉上了雙眼……\n")
                    time.sleep(3)
                    n += 1
                    Dead = True
                    continue
                print(f"\n不久後在島另一端的某棵大樹下，{Player[1:]}挖出了一個寶箱")
                print(f"裡面裝著{Item_5[0]}，總覺得在不久的將來會派上用場")
                Item_5[1] = True
                if Heroine == True: #真結局條件1
                    time.sleep(1)
                    print(f"同時寶箱內藏有一塊橡皮擦，感到困惑的我便拿給愛咪莉雅看")
                    time.sleep(1)
                    print(f"\n愛咪莉雅一眼便認出那是{Item_7[0]}，霎時潸然淚下")
                    time.sleep(1)
                    print("\n原來那是愛咪莉雅還在讀國中時，坐在左邊的男同學送給她的")
                    print(f"「謝謝你幫我找回這份寶貴的記憶，{Player[1:]}君」")
                    print(f"愛咪莉雅將{Item_7[0]}捧在掌心，追憶著過去上課時捉弄初戀的點點滴滴……")
                    Item_7[1] = True
                    time.sleep(2)
                else:
                    pass
                print(f"\n結束探索後{Player[1:]}稍作休息，便搭船返航準備繼續冒險")
                Ex_1 = True #去過+1
                time.sleep(2)
                continue
            else:
                print("那種鬼地方我不想再去第二次了，換個別的吧！")
                time.sleep(1)
                continue
        elif Choice_3 == "2": #卡美洛
            if Ex_2 == False:
                print(f"{Player[1:]}跨越國境來到大不列顛，在尋找卡美洛王國途中看到前方戰火紛飛")
                time.sleep(1)
                print("\n劍戟交鋒的荒野上，赫然發現亞瑟王被莫德雷德壓制而居於劣勢，是否該上前幫忙呢？")
                Choice_5 = input("1.協助亞瑟王  2.保護好自己  ：")
                if Choice_5 == "1": #選幫忙觸發事件
                    print(f"莫德雷德高舉聖劍克拉倫特，正準備砍向亞瑟王時卻查覺到{Player[1:]}的身影")
                    time.sleep(1)
                    if Item_4[1] == False and Heroine == False:
                        print(f"\n「別礙事！」一個側箭步莫德雷德轉身蹬向十幾公尺外的{Player[1:]}")
                        time.sleep(1)
                        print(f"\n「哪尼…？」認為自己有主角光環的{Player[1:]}(並沒有)，根本不是圓桌騎士的對手")
                        print(f"叛逆之心驅使著莫德雷德大開殺戒，一擊便刺中{Player[1:]}的心臟")
                        print(f"{Player[1:]}接受自己的命運，緩緩地閉上了雙眼……\n")
                        time.sleep(3)
                        n += 1
                        Dead = True
                        continue
                    else:
                        if Item_4[1] == True: #有道具優先擋死
                            print(f"\n{Player[1:]}將不久前拿到的{Item_4[0]}拋向亞瑟王")
                            time.sleep(1)
                            print(f"「別礙事！」一個側箭步莫德雷德轉身蹬向十幾公尺外的{Player[1:]}")
                            print("然而下一秒亞瑟王以更快的速度攔住莫德雷德，氣勢與方才判若兩人")
                            time.sleep(1)
                            print(f"\n如果誓約勝利之劍Excalibur是最強的矛，那麼與之成對的{Item_4[0]}便是最強的盾")
                            print(f"{Item_4[0]}能為亞瑟王提供強大的治癒之力，乃同名之「遙遠的理想鄉」的具現化")
                            time.sleep(1)
                            print("\n亞瑟王成功手刃其叛逆之子，為卡蘭姆之役畫下句點")
                            time.sleep(1)
                        else:
                            Heroine = False #無道具女主擋死
                            print(f"\n「別礙事！」一個側箭步莫德雷德轉身蹬向十幾公尺外的{Player[1:]}")
                            print("被莫德雷德的氣勢所震懾，我愣在原地雙腳不聽使喚，無法躲開")
                            time.sleep(1)
                            print(f"\n「Explosion!」站到{Player[1:]}面前的是愛咪莉雅，隨著她的詠唱莫德雷德被爆裂魔法炸飛")
                            print("然而聖劍克拉倫特仍刺中她的腹部，兩人同一時間雙雙倒下")
                            time.sleep(1)
                            print(f"\n「雖然相處時間不長，謝謝你出現在我的人生裡……{Player[1:]}君」")
                            print("奄奄一息的愛咪莉雅說完閉上了雙眼")
                            print("同時愛咪莉雅的犧牲，也為這場史詩般的戰役畫下句點")
                            time.sleep(2)
                elif Choice_5 == "2":
                    print("儘管屈居下風，亞瑟王仍氣勢不減，在防禦中尋找著反擊的機會")
                    print("兩人的動作快到無法看清，彷彿誰都無法任意插手")
                    time.sleep(1)
                    print("\n「完全是不同次元，幸好沒有過去送頭……」我在內心OS著")
                    time.sleep(1)
                    print("\n一瞬間亞瑟王抓住高文卿幫忙製造的間隙，將誓約勝利之劍刺向莫德雷德")
                    print("亞瑟王成功手刃其叛逆之子，為卡蘭姆之役畫下句點")
                    time.sleep(1)
                else:
                    print("看到眼前光景而愣住的當下，突然一把劍從背後刺進身體")
                    time.sleep(1)
                    print("\n高文卿以為你也是叛逆方的一份子，毫不猶豫地作為敵人排除")
                    print("猶如警示著你不要亂選答案般的一道神罰")
                    print(f"{Player[1:]}接受自己的命運，緩緩地閉上了雙眼……\n")
                    time.sleep(3)
                    n += 1
                    Dead = True
                    continue
                print("\n待一切安頓好之後，我前去拜見亞瑟王，並從他手中接過一個盒子")
                print(f"裡面裝著{Item_6[0]}，總覺得在不久的將來會派上用場")
                Item_6[1] = True
                if Heroine == True: #真結局條件2
                    time.sleep(1)
                    print("臨走前王的親信貝德維爾給了我一片CD，感到困惑的我便拿給愛咪莉雅看")
                    time.sleep(1)
                    print(f"\n愛咪莉雅一眼便認出那是{Item_8[0]}，霎時潸然淚下")
                    time.sleep(1)
                    print("\n原來愛咪莉雅畢業後曾加入草莓娛樂，夢想著在舞台上發光發熱")
                    print(f"愛咪莉雅將{Item_8[0]}捧在掌心，追憶著過去當偶像時的點點滴滴")
                    print(f"「謝謝你幫我找回這份寶貴的記憶，{Player[1:]}君」")
                    time.sleep(1)
                    print("\n「我愛你……現在終於能說出口，這句話絕對不是謊言呢」")
                    Item_8[1] = True
                    time.sleep(2)
                else:
                    pass
                print(f"\n結束探索後{Player[1:]}稍作休息，便啟程返航準備繼續冒險")
                Ex_2 = True #去過+1
                time.sleep(2)
                continue
            else:
                print("已經從亞瑟王那裡收到信物了，再換個地方吧！")
                time.sleep(1)
                continue
        elif Choice_3 == "3": #奧林帕斯
            print(f"在經歷幾番波折後，{Player[1:]}終於來到奧林帕斯山")
            print("這裡瀰漫著不祥的氣息，彷彿即將迎來最終決戰")
            time.sleep(1)
            print(f"\n「我已經在此等候多時了，異鄉的來者啊」原始神柯羅諾斯對{Player[1:]}說")
            print("「如果你能完成這十二道試煉，那麼時空之門將為你開啟」")
            print("語畢，柯羅諾斯將周圍空氣中的魔力流入手中，召喚出強大的希臘神")
            time.sleep(1)
            if Heroine == True: #有女主的額外劇情
                print(f"\n「抱歉了{Player[1:]}君，這裡的魔力不足以釋放爆裂魔法」")
                print("「不用擔心，我一定會保護你的」我緊握著愛咪莉雅的手迎接挑戰……")
                time.sleep(1)
            else:
                pass
            break #強制跳出二階迴圈
        else:
            print(f"\n邊想邊走的{Player[1:]}沒注意到腳下的樂高，踩下去痛到休克往生")
            print("猶如警示著你不要亂選答案般的一道神罰")
            print(f"{Player[1:]}接受自己的命運，緩緩地閉上了雙眼……\n")
            time.sleep(3)
            n += 1
            Dead = True
            continue
    if Dead == True: #二階死亡輪迴用
        continue
    else:
        pass
    #進入第三階段
    #玩家資料 = [名字,HP,ATK,暴擊ATK]
    Hero = [Player[1:],1000,200,260]
    Hero_ATK = [2,3]
    Hero_Weight = [0.8,0.2]
    #Boss資料 = [全名,略稱,HP,ATK]
    Boss_1 = ["爐灶女神．赫斯緹雅","赫斯緹雅",100,10]
    Boss_2 = ["傳令之神．荷米斯","荷米斯",200,50]
    Boss_3 = ["農業女神．狄蜜特","狄蜜特",300,50]
    Boss_4 = ["鍛造之神．赫淮斯托斯","赫淮斯托斯",400,100]
    Boss_5 = ["愛情女神．阿芙蘿黛蒂","阿芙蘿黛蒂",500,100]
    Boss_6 = ["月亮女神．阿提密斯","阿提密斯",600,150]
    Boss_7 = ["太陽之神．阿波羅","阿波羅",700,150]
    Boss_8 = ["戰爭之神．阿瑞斯","阿瑞斯",800,200]
    Boss_9 = ["智慧女神．雅典娜","雅典娜",900,200]
    Boss_10 = ["海洋之神．波賽頓","波賽頓",1000,250]
    Boss_11 = ["神譜統治．希拉","希拉",1100,250]
    Boss_12 = ["雷霆天神．宙斯","宙斯",1200,300]
    Boss_Fname = [Boss_1[0],Boss_2[0],Boss_3[0],Boss_4[0],Boss_5[0],Boss_6[0],Boss_7[0],Boss_8[0],Boss_9[0],Boss_10[0],Boss_11[0],Boss_12[0]]
    Boss_name = [Boss_1[1],Boss_2[1],Boss_3[1],Boss_4[1],Boss_5[1],Boss_6[1],Boss_7[1],Boss_8[1],Boss_9[1],Boss_10[1],Boss_11[1],Boss_12[1]]
    Boss_HP = [Boss_1[2],Boss_2[2],Boss_3[2],Boss_4[2],Boss_5[2],Boss_6[2],Boss_7[2],Boss_8[2],Boss_9[2],Boss_10[2],Boss_11[2],Boss_12[2]]
    Boss_ATK = [Boss_1[3],Boss_2[3],Boss_3[3],Boss_4[3],Boss_5[3],Boss_6[3],Boss_7[3],Boss_8[3],Boss_9[3],Boss_10[3],Boss_11[3],Boss_12[3]]
    Boss_hint = ["擺出戰鬥架式","改變氣場開始蓄力","按兵不動觀察局勢","眼神向後一撇"]
    Boss_act = ["普通攻擊","必殺技","防禦","逃跑"]
    HA_Rate = [0,1,2,3] #Boss動作指定
    Weight = [0.4,0.2,0.3,0.1] #權重
    Count = 0 #Boss出現次序
    Layer = 1 #當前試煉數
    if Fruit == True: #榴槤buff
        print("\n〈系統提示〉由於你先前取得榴槤，將自動裝備上並增加25%攻擊力")
        Hero[2] = Hero[2]*1.25
        Hero[3] = Hero[3]*1.25
        time.sleep(1)
    else:
        pass
    while Dead == False and Count <= 11:
        print(f"\n「歡迎來到第 {Layer} 道試煉，真虧你能走到這一步」") #每層遇敵
        print(f"「不過也就到此為止了，就由我 {Boss_Fname[Count]} 來當你的對手！」")
        time.sleep(1)
        while Hero[1] > 0 and Boss_HP[Count] > 0: #回合開始=準備階段
            print(f"\n{Hero[0]}當前血量：{Hero[1]}") #玩家血量狀態
            Hero_regen = 100 #回血數值
            HA_Choice = random.choices(HA_Rate,Weight)[0] #抽Boss動作
            print(f"{Boss_name[Count]}{Boss_hint[HA_Choice]}，{Hero[0]}思索片刻便決定——") #Boss動作提示
            Hero_Choice = input("1.普通攻擊  2.捨命攻擊  3.絕對防禦  ：") #玩家選擇=戰鬥階段
            if Hero_Choice =="1" or Hero_Choice == "2":
                Hero_CATK = random.choices(Hero_ATK,Hero_Weight)[0] #抽玩家是否暴擊
            else:
                pass                
            if HA_Choice == 3: #Boss逃跑
                print(f"\n{Boss_name[Count]}頓時感到不對勁，使出了 {Boss_act[HA_Choice]}")
                print(f"轉眼間{Boss_name[Count]}便消失無蹤，留下不知道發生什麼事的{Hero[0]}呆愣在原地")
                Boss_HP[Count] = 0
            else:
                if Hero_Choice == "1": #玩家普攻
                    if HA_Choice == 2: #Boss防禦                
                        print(f"\n{Hero[0]}發動普攻，但只對{Boss_name[Count]}造成 {Hero[Hero_CATK]*0.5} 點傷害！")
                        print(f"原來是{Boss_name[Count]}使出了{Boss_act[HA_Choice]}以抵擋部分攻擊")
                        Boss_HP[Count] = Boss_HP[Count] - Hero[Hero_CATK]*0.5
                    elif HA_Choice == 0: #Boss普攻
                        if Hero_CATK == 3: #暴擊判定
                            print(f"\n{Hero[0]}發動普攻，居然對{Boss_name[Count]}造成 {Hero[Hero_CATK]} 點暴擊傷害！")
                        elif Hero_CATK == 2:
                            print(f"\n{Hero[0]}發動普攻，對{Boss_name[Count]}造成 {Hero[Hero_CATK]} 點傷害！")
                        else:
                            pass
                        Boss_HP[Count] = Boss_HP[Count] - Hero[Hero_CATK]
                        if Boss_HP[Count] <= 0:
                            continue
                        else:
                            print(f"{Boss_name[Count]}也使出了{Boss_act[HA_Choice]}，對{Hero[0]}造成 {Boss_ATK[Count]} 點傷害")
                            Hero[1] = Hero[1] - Boss_ATK[Count]
                    elif HA_Choice == 1: #Boss必殺
                        if Hero_CATK == 3:
                            print(f"\n{Hero[0]}發動普攻，居然對{Boss_name[Count]}造成 {Hero[Hero_CATK]} 點暴擊傷害！")
                        elif Hero_CATK == 2:
                            print(f"\n{Hero[0]}發動普攻，對{Boss_name[Count]}造成 {Hero[Hero_CATK]} 點傷害！")
                        else:
                            pass
                        Boss_HP[Count] = Boss_HP[Count] - Hero[Hero_CATK]
                        if Boss_HP[Count] <= 0:
                            continue
                        else:
                            print(f"然而{Boss_name[Count]}也使出了{Boss_act[HA_Choice]}，對{Hero[0]}造成 {Boss_ATK[Count]*1.5} 點巨額傷害")
                            Hero[1] = Hero[1] - Boss_ATK[Count]*1.5
                    else:
                        pass
                elif Hero_Choice == "2": #玩家大招
                    if HA_Choice == 2: #Boss防禦                        
                        print(f"\n{Hero[0]}犧牲一半的血量發動捨命攻擊，但只對{Boss_name[Count]}造成 {Hero[Hero_CATK]*0.5*2} 點傷害！")
                        print(f"原來是{Boss_name[Count]}使出了 {Boss_act[HA_Choice]} 抵擋部分攻擊")
                        Boss_HP[Count] = Boss_HP[Count] - Hero[Hero_CATK]*0.5*2
                        Hero[1] = Hero[1]*0.5
                    elif HA_Choice == 0: #Boss普攻
                        if Hero_CATK == 3:
                            print(f"\n{Hero[0]}犧牲一半的血量發動捨命攻擊，居然對{Boss_name[Count]}造成 {Hero[Hero_CATK]*2} 點暴擊傷害！")
                        elif Hero_CATK == 2:    
                            print(f"\n{Hero[0]}犧牲一半的血量發動捨命攻擊，對{Boss_name[Count]}造成 {Hero[Hero_CATK]*2} 點巨額傷害！")
                        else:
                            pass
                        Boss_HP[Count] = Boss_HP[Count] - Hero[Hero_CATK]*2
                        Hero[1] = Hero[1]*0.5
                        if Boss_HP[Count] <= 0:
                            continue
                        else:
                            print(f"{Boss_name[Count]}也使出了{Boss_act[HA_Choice]}，對{Hero[0]}造成 {Boss_ATK[Count]} 點傷害")
                            Hero[1] = Hero[1] - Boss_ATK[Count]
                    elif HA_Choice == 1: #Boss必殺
                        if Hero_CATK ==3:
                            print(f"\n{Hero[0]}犧牲一半的血量發動捨命攻擊，居然對{Boss_name[Count]}造成 {Hero[Hero_CATK]*2} 點暴擊傷害！")
                        elif Hero_CATK ==2:
                            print(f"\n{Hero[0]}犧牲一半的血量發動捨命攻擊，對{Boss_name[Count]}造成 {Hero[Hero_CATK]*2} 點巨額傷害！")
                        else:
                            pass
                        Boss_HP[Count] = Boss_HP[Count] - Hero[Hero_CATK]*2
                        Hero[1] = Hero[1]*0.5
                        if Boss_HP[Count] <= 0:
                            continue
                        else:
                            print(f"然而{Boss_name[Count]}也使出了{Boss_act[HA_Choice]}，對{Hero[0]}造成 {Boss_ATK[Count]*1.5} 點巨額傷害")
                            Hero[1] = Hero[1] - Boss_ATK[Count]*1.5
                    else:
                        pass
                elif Hero_Choice == "3": #玩家防禦
                    if HA_Choice == 2: #Boss防禦
                        if Hero[1] > 900: #判定是否溢補
                            Hero_regen = 1000- Hero[1]
                        else:
                            Hero_regen = 100
                        print(f"\n{Hero[0]}發動絕對防禦，採取守備狀態並恢復 {Hero_regen} 點血量！")
                        print(f"{Boss_name[Count]}也使出了{Boss_act[HA_Choice]}，雙方僵持不下")
                        Hero[1] = Hero[1] + Hero_regen
                    elif HA_Choice == 0: #Boss普攻
                        if Hero[1] > 900:
                            Hero_regen = 1000- Hero[1]
                        else:
                            Hero_regen = 100
                        print(f"\n{Hero[0]}發動絕對防禦，採取守備狀態並恢復 {Hero_regen} 點血量！")
                        print(f"{Boss_name[Count]}也使出了{Boss_act[HA_Choice]}，對{Hero[0]}造成 {Boss_ATK[Count]*0.5} 點傷害")
                        Hero[1] = Hero[1] + Hero_regen                       
                        Hero[1] = Hero[1] - Boss_ATK[Count]*0.5
                    elif HA_Choice == 1: #Boss必殺
                        if Hero[1] > 900:
                            Hero_regen = 1000- Hero[1]
                        else:
                            Hero_regen = 100
                        print(f"\n{Hero[0]}發動絕對防禦，採取守備狀態並恢復 {Hero_regen} 點血量！")
                        print(f"然而{Boss_name[Count]}也使出了{Boss_act[HA_Choice]}，對{Hero[0]}造成 {Boss_ATK[Count]*1.5*0.5} 點傷害")
                        Hero[1] = Hero[1] + Hero_regen
                        Hero[1] = Hero[1] - Boss_ATK[Count]*1.5*0.5
                    else:
                        pass
                else:
                    print(f"\n看著眼前不同次元的對手，想轉身就跑的{Hero[0]}卻因踩到香蕉皮滑倒重擊頭部")
                    print("猶如警示著你不要亂選答案般的一道神罰")
                    time.sleep(1)
                    Hero[1] = 0
                    break #強制回合結束
        if Hero[1] <= 0: #死亡結算階段
            time.sleep(1)
            print("「……果然還是沒辦法嗎」")
            print(f"\n{Hero[0]}因血量歸零而奄奄一息，於接受自己的命運後緩緩地閉上了雙眼……\n")
            n += 1
            Dead = True
            continue
        else: #打贏戰鬥結算
            time.sleep(1)
            print(f"\n在這拳拳到肉的纏鬥中，{Hero[0]}以些微的差距險勝")
            if Heroine == True: #有女主的額外劇情
                print(f"「{Hero[0]}君！」愛咪莉雅上前抱住搖搖欲墜的{Hero[0]}")
                print(f"在接受魔法治療後，{Hero[0]}起身繼續戰鬥")
            else:
                print(f"在喝完恢復藥水後，{Hero[0]}起身繼續戰鬥")
            Hero[1] = 1000
            time.sleep(1)
            if Item_5[1] == True:
                if Count == 0 or Count == 2 or Count == 4:
                    print(f"\n這時在不久前拿到的 {Item_5[0]} 突然發光，似乎有什麼神奇的效果發生了")
                    Count += 1
                    Layer += 1
                    time.sleep(1)
                else:
                    pass
            else:
                pass
            if Item_6[1] == True:
                if Count == 6 or Count == 8:
                    print(f"\n這時在不久前拿到的 {Item_6[0]} 突然發光，似乎有什麼神奇的效果發生了")
                    Count += 1
                    Layer += 1
                    time.sleep(1)
                else:
                    pass
            else:
                pass
            Count += 1
            Layer += 1
    if Dead == True: #戰鬥死亡輪迴用
        continue
    else:
        pass   
    #終幕
    time.sleep(1)
    print("\n「能完成十二道試煉的，至今就只有你一個」柯羅諾斯說完便開啟時空之門")
    print(f"只要從這道門進入，便能回歸原來的生活，這也是一路走來的目的")
    print("在走進傳送門的前一刻，我突然停下腳步並回首……")
    time.sleep(1)
    True_end = "隱藏結局"
    Normal_end = "普通結局"
    if Item_7[1] == True and Item_8[1] == True:
        print("\n「這段旅程真的很快樂，你願意跟我繼續旅行嗎？」我朝著愛咪莉雅伸出手") #真結局
        time.sleep(1)
        print(f"\n「從我失去記憶以來，每天都迷惘著找不到前進的動力」")
        time.sleep(1)
        print(f"「凍結的心，是{Hero[0]}君的溫暖將其融化的」")
        print(f"「停止的時間，是{Hero[0]}君的溫柔使其開始轉動」")
        time.sleep(1)
        print(f"\n「只要有{Hero[0]}君的陪伴，無論去哪裡我都願意」")
        print(f"愛咪莉雅說完便牽起我的手，兩人一起步入傳送門，準備在{Hero[0]}的世界展開全新的旅程")
        print(f"\n{True_end:*^24s}")
    else:
        if Heroine == True: #與女主道別後進普通結局
            print("\n「雖然相處時間不長，但我不會忘記這段與你共度的旅程」")
            print(f"「謝謝你{Hero[0]}君，我也會將這份回憶永存在心底」")
            time.sleep(1)
        else:
            pass
        print("\n回想一路走來的點點滴滴，依稀覺得好像錯過了什麼") #普通結局
        print("但還是邁開步伐，再一次跟這個世界道別")
        print(f"\n{Normal_end:*^24s}")
    time.sleep(1)
    print(f"\n〈系統提示〉至今為止您總共體驗了 {n} 次死亡輪迴")
    Again = input("\n是否要再玩一次呢？ 1.是  2.否  ：")
    if Again == "1":
        time.sleep(1)
        continue
    elif Again == "2":
        print("\n感謝您的遊玩！")
        break
    else:
        print("\n都玩到這裡了還要亂選啊，再讓你死一次")
        n += 1
        Dead = True
        continue
