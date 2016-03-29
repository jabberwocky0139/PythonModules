# coding: utf-8
import os

""" ----------- Read me! -------------

Cythonをかんたんに使うべく作られたラッパーです. 改善の余地まだまだあり. 使用したいソースコードにて継承して使用してください. コンストラクタには

def __init__(filename, dirpath, methodtest, c_remove, procedure)

の3つを渡してください. 

・filename : string型. 作成するモジュール名を拡張子なしで代入. 
・dirpath : 現在編集中のファイルがあるディレクトリ名を絶対パスで代入. 最後の"/"は要りません.
・methodtest : デフォルトでFalseがセットされているので渡さなくても良い. Trueにするとsandbox_for_making_method()を実行します(後述). 
・pyx_remove, c_remove : デフォルトでTrue. Cythonビルドの際に作られる .pyx, .cファイルを削除するかどうかを選択できます. 

コンストラクタはスーパークラスで定義されているので, サブクラスでのコンストラクタのオーバーライドは絶対に行わないでください(継承した側のクラスにはコンストラクタは作らないでください). 
スーパークラスには2つの純粋仮想関数があります. 

・sandbox_for_making_method() : pyx_string_generator()にソースコードを埋め込む前に実行テストができるsandboxです. こちらにはcdef int の定義は含めないでください. 
・procedure() : ライブラリをimportして実行するメソッド. コンストラクタ引数のprocedureがTrueならインスタンス作成時に実行されます. 

小クラスのインスタンスを作成するとCythonのビルドまでが完了します. ビルドが完了すると

======= Succeeded! =======

と表示されます. インスタンスを作成した直下でモジュールfilenameをimportしてください. これでfilename下の関数が使用できます. 

----------- Read me! ------------- """ 
# generate "setup.py" and build module
class CythonWrapper:
    # filename : <filename>.pyx, string
    # dirpath : fullpath, string
    def __init__(self, filename, dirpath, methodtest=False, c_remove=True, procedure=True):
        self.filename = filename
        self.dirpath = dirpath
        self.setup_generator()
        if methodtest:
            print("====== method test ======\n")
            self.sandbox_for_making_method()
            print("\n====== end method test ======")
        if c_remove:
            os.system("sudo rm " + self.filename + ".c")
        if procedure:
            self.procedure()
            
        
    def setup_generator(self):
        f = open(self.dirpath + "/setup.py", "w")
        print("##### setup.py", file=f)
        print("from distutils.core import setup", file=f)
        print("from distutils.extension import Extension", file=f)
        print("from Cython.Distutils import build_ext", file=f)
        print("", file=f)
        print("ext_modules = [Extension('" + self.filename + "', ['" + self.filename + ".pyx'])]   #assign new.pyx module in setup.py.", file=f)
        print("setup(name        = '" + self.filename + " app',cmdclass    = {'build_ext':build_ext},ext_modules = ext_modules)", file=f)
        print("", file=f)
        print("##### end", file=f)
        f.close()
        #os.system("touch " + self.dirpath + "hogehoge.txt")
        info1 = os.system("sudo python3 " + self.dirpath + "/setup.py build_ext")
        info2 = os.system("sudo python3 " + self.dirpath + "/setup.py install_lib")
        info3 = os.system("sudo rm " + self.dirpath + "/setup.py")
        if info1 == info2 == info3 == 0:
            print("====== Succeeded! ======")
        else:
            print("====== Something error occured! ======")


    # for override(virtual function)
    def sandbox_for_making_method(self):
        pass
    
    # for override(virtual function)
    def procedure(self):
        import hogehoge
        mogemoge.module()
    
