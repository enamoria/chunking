# coding=utf-8
import os
import sys

from src.CONSTANT import ROOT_DIR


class Reader:
    """
        Reader for multiple format
    """

    def __init__(self, rel_data_path, description=None):
        self.datapath = ROOT_DIR + rel_data_path
        print(self.datapath)

        if description is not None:
            print(description)

        # raise NotImplementedError

    def check_valid(self):
        return True

    def reader_10000(self):
        """
            read the whole file of the whole directory into a list of list:
            list of sentences (each sentence is list of words)
        :return: list of sentences
        """

        print("=======================================")

        print("Start reading 'vi' data ...")

        filelist = sorted(os.listdir(self.datapath))

        data = []  # data will be stored here

        for file in filelist:
            with open(self.datapath + "/" + file, "r") as f:
                raw_text = f.read().strip("\n").strip(" ").replace("\n", " ")
                raw_text = "BEGIN/BEGIN " + raw_text + " END/END"
                raw_text = raw_text.replace("   ", " ").replace("  ", " ")
                data.append(raw_text.split(" "))

        print("Done reading 'vi' data,", len(data), "file found")

        for i in range(len(data)):
            for word in data[i]:
                if len(word.split("/")) != 2:
                    print("xxx", filelist[i], word)
            data[i] = [word.split("/") if word != "/" else ['/', '/'] for word in data[i]]

        # assert self.isNormalized(data), "Data is not refined, need to be preprocess. Exiting ... "

        return data

        # raise NotImplementedError

    def reader_VLSP(self):

        print("=======================================")

        print("Start reading 'VLSP' data in", self.datapath, "...")

        filelist = sorted(os.listdir(self.datapath))
        # print(filelist)
        # input("...")

        data = []  # data will be stored here

        for file in filelist:
            with open(self.datapath + "/" + file, "r") as f:
                raw_text = f.read().strip("\n").strip(" ").replace("\n", " ")
                raw_text = "BEGIN/BEGIN " + raw_text + " END/END"
                raw_text = raw_text.replace("   ", " ").replace("  ", " ")
                data.append(raw_text.split(" "))

        print("Done reading 'VSLP' data,", len(data), "file found")

        for i in range(len(data)):
            for word in data[i]:
                if len(word.split("/")) != 2 and word[0] != '/':
                    print("yyy", filelist[i], word)
            data[i] = [word.split("/") if word[0] != "/" else ['/', 'CH'] for word in data[i]]

        # print("Not implemented yet ...")
        # return None

        return data
        # raise NotImplementedError

    def reader_conll2003(self):
        print("Not implemented yet ...")
        # return None
        raise NotImplementedError

    def read(self, dataset='10000'):
        print("Start checking if data", dataset, "is valid/supported or not ...")

        if self.check_valid():
            print("Done checking, everything looks good")
        else:
            print("Something wrong, recheck your data")
            sys.exit()

        options = {'10000': self.reader_10000, 'en': self.reader_conll2003, 'VLSP': self.reader_VLSP}

        try:
            return options[dataset]()
        except KeyError:
            print(dataset, "not found")
            print("Available dataset:", options.keys())
            print("Exiting ...")
            sys.exit()

    def normalize(self, data):
        print("=======================================")
        print("Runing normalize ... Old data will be overwritten")
        filelist = sorted(os.listdir(self.datapath))
        for index, sentence in enumerate(data):
            # print(sentence)
            # words = [word.split("/")[1] for word in sentence]
            #     print(index, word, sentence[idx + 1], filelist[index])
            f_index = open(self.datapath + "/" + filelist[index])
            xxx = f_index.read()
            f_index.close()

            f_index = open(self.datapath + "/" + filelist[index], "w")

            xxx = xxx.replace(':Lời/N', ': Lời/N')

            xxx = xxx.replace('vì sao/X', 'vì_sao/X')
            xxx = xxx.replace('Vì sao/X', 'Vì_sao/X')

            xxx = xxx.replace('một số/X', 'một_số/X')
            xxx = xxx.replace('một số/L', 'một_số/L')
            xxx = xxx.replace('Một số/L', 'Một_số/L')

            xxx = xxx.replace('Một số/X', 'Một_số/X')
            xxx = xxx.replace('phóS', 'phó/S')
            xxx = xxx.replace('thủy_ hải_sản', 'thủy_hải_sản')

            xxx = xxx.replace("chục triệu", "chục/M triệu")
            xxx = xxx.replace("liền kề", "liền_kề")

            xxx = xxx.replace("như vậy", "như_vậy")
            xxx = xxx.replace("như thế", "như_thế")
            xxx = xxx.replace("thế này", "thế_này")

            xxx = xxx.replace("conNc gái/N", "con/Nc gái/N")

            xxx = xxx.replace("Vậy là/C", "Vậy_là/C")
            xxx = xxx.replace("Dẫu vậy/C", "Dẫu_vậy/C")

            xxx = xxx.replace("nhắc đi nhắc lại", "nhắc_đi_nhắc_lại")
            xxx = xxx.replace("mở đi mở lại", "mở_đi_mở_lại")
            xxx = xxx.replace("chưa thể", "chưa_thể")
            xxx = xxx.replace("lặp đi lặp lại", "lặp_đi_lặp_lại")
            xxx = xxx.replace("thâu đêm suốt sáng", "thâu_đêm_suốt_sáng")

            xxx = xxx.replace("ba chục", "ba_chục")

            xxx = xxx.replace("không những", "không_những")
            xxx = xxx.replace("anhN ta/P", "anh/N ta/P")
            xxx = xxx.replace("Mercedes E240", "Mercedes_E420")
            xxx = xxx.replace("Không_ thể_nào", "Không_thể_nào")

            xxx = xxx.replace("thế này/X", "thế_này/X")
            xxx = xxx.replace("một cách/N", "một_cách/N")
            xxx = xxx.replace("không thể_nào/R", "không_thể_nào/R")
            xxx = xxx.replace("biếtV bao/L", "biết/V bao/L")
            xxx = xxx.replace("không_ thể_nào", "không_thể_nào")
            xxx = xxx.replace("chẳng_ bao_giờ", "chẳng_bao_giờ")
            xxx = xxx.replace("cây_ ăn_trái", "cây_ăn_trái")
            xxx = xxx.replace("Vì răng", "Vì_răng")

            xxx = xxx.replace("không chỉ/C", "không_chỉ/C")
            xxx = xxx.replace("quaV một/M", "qua/V một/M")
            xxx = xxx.replace("giúp việc/V", "giúp_việc/V")
            xxx = xxx.replace("tổng số/N", "tổng_số/N")
            xxx = xxx.replace("người bệnh/N", "người_bệnh/N")
            xxx = xxx.replace("một cách/N", "một_cách/N")

            xxx = xxx.replace("biếtV bao/L", "biết/V bao/L")
            xxx = xxx.replace("TP. HCM/Ny", "TP._HCM/Ny")
            xxx = xxx.replace("TP._HCM/Np", "TP._HCM/Np")
            xxx = xxx.replace("cóRV biết/V", "có/RV biết/V")

            xxx = xxx.replace("ví như/X", "ví_như/X")

            xxx = xxx.replace("Nam Đ./Ny", "Nam_Đ./Ny")
            xxx = xxx.replace("Pháp/Np - Việt/Np", "Pháp/Np -/- Việt/Np")
            xxx = xxx.replace("Việt/Np - Lào/Np", "Việt/Np -/- Lào/Np")

            xxx = xxx.replace("trung_ ứng/N", "trung_ứng/N")
            xxx = xxx.replace("Nào ngờ", "Nào_ngờ")
            xxx = xxx.replace("kỳ_ nữ/N", "kỳ_nữ/N")
            xxx = xxx.replace("dầu ăn/N", "dầu_ăn/N")

            xxx = xxx.replace("đầuN bảng/N", "đầu/N bảng/N")

            xxx = xxx.replace("TP/Ny (. .) HCM/Ny", "TP._HCM/Ny")
            xxx = xxx.replace("P/Ny (. .) 12/M ,/, Q/Ny (. .)", "P/Ny 12/M ,/, Q/Ny ")
            xxx = xxx.replace(" (. .) ", " ")
            xxx = xxx.replace("trưởngN ban/N", "trưởng/N ban/N")
            xxx = xxx.replace("TP. HCM", "TP._HCM")

            xxx = xxx.replace("TP.  HCM/Ny", "TP._HCM/Ny")
            xxx = xxx.replace("4M -/-1999/M", "4/M -/-1999/M")
            xxx = xxx.replace("6M -/-", "6/M -/-")
            xxx = xxx.replace("con/ Nc gái/N", "con/Nc gái/N")
            xxx = xxx.replace("13/M - 7/M", "13/M -/- 7/M")

            xxx = xxx.replace("!/!”/”", "!/! ”/”")
            xxx = xxx.replace("!/!(/(", "!/! (/(")

            xxx = xxx.replace("!/!\"/\"", "!/! \"/\"")
            xxx = xxx.replace("!/!”/”", "!/! ”/”")

            xxx = xxx.replace("N/vai/V", "vai/N")
            xxx = xxx.replace("được/Vdọn/V", "được/V dọn/V")
            xxx = xxx.replace(":/:Những/L", ":/: Những/L")
            xxx = xxx.replace("tới/Tbốn/M", "tới/T bốn/M")
            xxx = xxx.replace("bò/Nđược/V", "bò/N được/V")
            xxx = xxx.replace("sau/Eđó/P", "sau/E đó/P")
            xxx = xxx.replace("lắc/V,/,", "lắc/V ,/,")
            xxx = xxx.replace("sau/Emột/M đêm/N", "sau/E một/M đêm/N")

            xxx = xxx.replace("../...Đó/P là/V", "../... Đó/P là/V")
            xxx = xxx.replace("hai/m", "hai/M")
            xxx = xxx.replace("hàng/Rchục/M mẫu_mã/N", "hàng/R chục/M mẫu_mã/N")
            xxx = xxx.replace(" :/:Tầng/N địa_ngục/N", " :/: Tầng/N địa_ngục/N")
            xxx = xxx.replace("sửa_chữa/V_lớn/A", "sửa_chữa/V lớn/A")
            xxx = xxx.replace("Ch/Np ./.đây/P ,/, tìm/V", "Ch/Np ./. đây/P ,/, tìm/V")

            xxx = xxx.replace("Ch./Np-/-", "Ch./Np -/-")
            xxx = xxx.replace("lui/R./.", "lui/R ./.")
            xxx = xxx.replace("U/Y-18/M", "U/Y 18/M")
            xxx = xxx.replace("vào/V./.", "vào/V ./.")
            xxx = xxx.replace("đ/Nu,/,", "đ/Nu ,/,")
            xxx = xxx.replace("được/Vdọn/V", "được/V dọn/V")
            xxx = xxx.replace("quán/N bar/Nb,/,", "quán/N bar/Nb ,/,")
            xxx = xxx.replace("./.đây/P ,/, tìm/V", "./. đây/P ,/, tìm/V")
            xxx = xxx.replace("lui/R./.", "lui/R ./.")
            xxx = xxx.replace("em/N U/Y-18/M", "em/N U/Y 18/M")
            xxx = xxx.replace("“/“ điều/V ”/” vào/V./.", "“/“ điều/V ”/” vào/V ./.")
            xxx = xxx.replace("100.000/M đ/Nu,/,", "100.000/M đ/Nu ,/,")

            xxx = xxx.replace("2/M -/-1943/M ./.", "2/M -/- 1943/M ./.")
            xxx = xxx.replace("có_thể/A làm/V_khách/N", "có_thể/A làm/V khách/N")
            xxx = xxx.replace(",/,Va/Np nói/V", ",/, Va/Np nói/V")
            xxx = xxx.replace("năm/N sau/A./.", "năm/N sau/A ./.")

            xxx = xxx.replace("Malaysia/Np chơi/V_xấu/A", "Malaysia/Np chơi/V xấu/A")
            xxx = xxx.replace("-/-1966/M", "-/- 1966/M")
            xxx = xxx.replace("18/M năm/N sau/A,/,", "18/M năm/N sau/A ,/, ")
            xxx = xxx.replace("cầu/_vương/N ”/” Lý_Huệ_Đường/Np(/( Hong_Kong/Np )/)",
                              "cầu_vương/N ”/” Lý_Huệ_Đường/Np (/( Hong_Kong/Np )/)")
            xxx = xxx.replace("bóng_bàn/N VN/Np./.", "bóng_bàn/N VN/Np ./.")
            xxx = xxx.replace("mạ/V vàng/N,/,", "mạ/V vàng/N ,/,")
            xxx = xxx.replace("?/?”/”", "?/? ”/”")
            xxx = xxx.replace(":/:Tận_diệt/V", ":/: Tận_diệt/V")

            xxx = xxx.replace(":/:“/“", ":/: “/“")
            xxx = xxx.replace("đồng/Nu ]/]nhà/N", "đồng/Nu ]/] nhà/N")
            xxx = xxx.replace("đánh/V_cá/N", "đánh/V cá/N")
            xxx = xxx.replace("đồng/Nu ]/]tháng/N ./.", "đồng/Nu ]/] tháng/N ./.")
            xxx = xxx.replace("-/-1999/M tại/E", "-/- 1999/M tại/E")
            xxx = xxx.replace("-/-_2002/M phải/V", "-/- 2002/M phải/V")
            xxx = xxx.replace("5/M -/-2002/M", "5/M -/- 2002/M")
            xxx = xxx.replace(")/): Những/L", ")/) :/: Những/L")
            xxx = xxx.replace("đi/R.../...", "đi/R .../...")
            xxx = xxx.replace("13/M -/-8 -/- ", "13/M -/- 8M -/- ")
            xxx = xxx.replace("ra/V nhỉ/T?/?", "ra/V nhỉ/T ?/?")

            xxx = xxx.replace("(./.)", "(/( ./. )/)")
            xxx = xxx.replace("[?/?]", "[/[ ?/? ]/]")
            xxx = xxx.replace("27-/-7/M ./.", "27/M -/- 7/M ./.")
            xxx = xxx.replace("Ngày/N 13/M-/- 9/M ", "Ngày/N 13/M -/- 9/M ")
            xxx = xxx.replace(" 4/M -/-1999/M tại/", " 4/M -/- 1999/M tại/")
            xxx = xxx.replace("?/?”/”", "?/? ”/”")
            xxx = xxx.replace("“/“ cầu/_vương/N ”/”", "“/“ cầu_vương/N ”/”")
            xxx = xxx.replace("-/-1966/M ", "-/- 1966/M ")
            xxx = xxx.replace("VN/Np,/, dù/C", "VN/Np ,/, dù/C")
            xxx = xxx.replace("chiến_thắng/N,/,", "chiến_thắng/N ,/,")
            xxx = xxx.replace("20/M tuổi/Nu./.", "20/M tuổi/Nu ./.")
            xxx = xxx.replace("Ch/Np ./.đây/P ,/,", "Ch/Np ./. đây/P ,/,")
            xxx = xxx.replace("sắt/N thép/N./.", "sắt/N thép/N ./.")

            xxx = xxx.replace("100/M %/Nu/M xã/N", "100/M %/Nu xã/N")
            xxx = xxx.replace("%/Nu/M", "%/Nu")
            xxx = xxx.replace("quản_lý//N", "quản_lý/N")

            xxx = xxx.replace("xuống//V", "xuống/V ")
            xxx = xxx.replace("sexy/Nb/?", "sexy/Nb ?/?")
            xxx = xxx.replace("fan/Nb/”", "fan/Nb ”/”")
            xxx = xxx.replace("cái//Nc", "cái/Nc")
            xxx = xxx.replace("đôi_khi/", "đôi_khi/N")

            xxx = xxx.replace("khắp/ mọi/A", "khắp/A mọi/A")
            xxx = xxx.replace("20/ triệu/M", "20/M triệu/M")
            xxx = xxx.replace("18/ -/- 9/M -/- 2005/M", "18/M -/- 9/M -/- 2005/M")
            xxx = xxx.replace("./\n", "./.\n")
            # xxx = xxx.replace("", "")
            # xxx = xxx.replace("", "")
            # xxx = xxx.replace("", "")
            # xxx = xxx.replace("", "")
            # xxx = xxx.replace("", "")
            # xxx = xxx.replace("", "")
            # xxx = xxx.replace("", "")

            f_index.write(xxx)
            f_index.close()

        print("Done normalizing!")

    def isNormalized(self, data):
        filelist = sorted(os.listdir(self.datapath))
        flag = True
        for index, sentence in enumerate(data):
            # print(sentence)
            # words = [word.split("/")[1] for word in sentence]
            words = []

            for idx, word in enumerate(sentence[0:len(sentence) - 1]):
                try:
                    word = word.strip(" ")
                    if word == "/":
                        words.append(['/'])
                        continue

                    words.append(word.split("/")[1])
                except IndexError:
                    flag = False
                    print(index, word, sentence[idx + 1], filelist[index])
                    self.normalize(data)
        return flag


if __name__ == "__main__":
    print(ROOT_DIR)
    reader = Reader("/data/data_POS_tag_tieng_viet", "ngu lieu pos tagging tieng viet")

    data = reader.read('10000')
    print(data[1])
