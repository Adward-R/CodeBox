__author__ = 'Adward'
from time import time
class Solution(object):
    def maxProduct0(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        t = time()
        words.sort(key=lambda w: len(w), reverse=True)
        #print(words)

        letterIndex = [set() for i in range(26)]
        for i in range(len(words)):
            for ch in words[i]:
                letterIndex[ord(ch)-ord('a')].add(i)

        print(letterIndex)
        cps = [[1] * len(words) for i in range(len(words))]
        for letter in letterIndex:
            letter = list(letter)
            for i in range(len(letter)-1):
                for j in range(i+1, len(letter)):
                    cps[letter[i]][letter[j]] = 0

        #print(cps)
        maxPro = 0
        for i in range(len(words)-1):
            if len(words[i]) * len(words[i+1]) <= maxPro:
                break
            for j in range(i+1, len(words)):
                if cps[i][j]:
                    maxPro = max(maxPro, len(words[i]) * len(words[j]))
                    break
        print(time()-t)
        return maxPro

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        t = time()
        curr_max = 0
        for i in range(len(words)):
            curr_word = set(words[i])
            curr_len = len(words[i])
            for word in words[i+1:]:
                for ch in curr_word:
                    if ch in word:
                        break
                else:
                    curr_max = max(curr_max, curr_len * len(word))
        print(time()-t)
        return curr_max

sol = Solution()
#words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
#words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
#words = ["a", "aa", "aaa", "aaaa"]
#words = ["ecgfdcgebbafecacccgacaedcbdcfbdfffebf","gecgeebagagdaabggfafdcdgcfcaccecebabcgeaaegdddgdcdgdfcfbecbbabcbcdafageegagaafcfafedbfagagdddega","dbdfafbdfaefacfgaafggefcbfdgddbecaccgeabgfdbebbcfcceabagcfccecggdbbgcgcabdebdfdbc","egdfgfcafbbaegagcgecddagcbgbgabegbbbcbcgcagecdfbgdca","cgadcgabagcabfeccafccdebggc","adgceaeegegegafcc","efgfcfadegeccfgdfbdafccgecedgbeegbcfcgaeeef","deacgecfddacg","faggeaeeaaeagedeeacgageabedggeacdecdbecgfbbbgcacdcdgbcaffdcfadfbbgggedcdfgeaddagfcffccffcfff","fbabdfegbdbfcgecbeaagcdfffbdbabdggagggfdgddgfcegba","gdgcgfgfbbeddbdfabdebbgeeccabccgcaddgadabeecefgcbbcdbbdffdfeaeebaccfadadbeagccefegfcdgdee","ffeddedbffgbageebfadbedafbgggdaegbddcbgcceccecggb","acbadggdagbdccbcbabeddbcefegddcacaddacedbfbfbcdbaccabffbgggaebdceefcaggbfeegef","acebbebacccecgeccfaecadgfgdbggcdgedcggbdaadagag","fdgeedggfcfcdfbbfccbfabfbecfbadccfcgdefcddcagbddagfadbdgbabeggfbacebcfecaaacgcbfefgbg","aabegbcgfgcfgdfcggeedgfggdbbcedecccddcbgaedgdgebbfgbcfaaedefeggcggcfedbfcagegdbcdcfaccedgebgfc","beaabcbegcebbcdgbfbaecddedbgdaededdecgcebadcggfcgefcb","agfgdecgdeeecaagbbgcadaaeffcffaebba","ededababdgbbbgdfbdgafaeageedbafabccecgfcfgcdebcfcadbdedeccgfefecgcgc","eeafdefbdbbbddegddacabdacbdgddccbedfdbfcddfggdbgedecdbfcffagadaddfdaac","egffcadagdedfeegebbfgdffgdgabbaeeedebcgfabeafebgbgbfcbaddadagdfceggcffgcabffggdbdcggfeacegfd","ebbbafbfeaegaggfaaccgfgfaeccbgfafegfcbdaddafcc","ffddfggebded","bcbbbafefafadbefdgddffdacgbcaaadfeggdgeccefegceccabeababgbaggbcaceccecbfecge","bgdacefeedcfagadbcedcfaafggebcc","eceaddabcbgaffcf","fcgefcdgcffbfedebbb","baecgaffcdgfceggebbacfabgabebeecegfffcdfgafagecfdbbefadabgcdggecebbdadaegaadeebddbefgbd","cebgagg","ddaffbddfbedbcgbeegbgfffcbdafgadgg","gecdbaaacaeafaecdgbefbcedfbffgfbdacfgceebeeagfabedadbcdb","cfdeede","fcdcacedbaabgdfeebeffffgfgecgfgacdcdecfefeaggb","cdbfddecegabadggfadcgdbfeafdbccgbebgbfedgffabgdcfdeaadacbee","ebdgdddagcbbbaeddececgfegebcbfccffgbafegbcbabegcbgfagcaaba","fbcbccacdagdagfebccdeafdfcbggecf","fgfaggafbbacedggdaadgcgdeeaggefgdd","ecgbadaaacgccfdggdcfbead","bcfcbgeac","bafdcecbbaegbaacfgegdbcfgabfacccbebbafebcdagcadgbaebcdfdceeeaggaacggdgdagedbbcbadfcdgggfaffbagddfg","bfaeegbbcbcgbbaefababfdfgffcbacafebaefbedcaeaagcagefceeeacbaadecdcb","dddcaedagbbefdcdddcfbbd","dfgegggfcgaeaaafbaeafgbedcbacgbdgadccafeecdbceb","ccdaafabadgafggffgfdaecggaagaaacgfecddaagbedeggbaaccgbdebegccaebeabggcbbgffbedgecfgdfegadbfgaceggb","bgcdfbfbcccdaccbgddcadeecfbedd","badbbgdefdabgbeagfccdcbgeeaabaccbbcedfdeafabfaacfcbgbgbcbecddagcebafecfabffeb","afegdefggdabefd","egabbcbebebbcbgffgecafgccaafdfdfefgdedeadacadabegcgedgafeefgafaedbdacabccceeedde","abebbdecdeeabbgcacgeafdbcbfdabggaefgeefefgcdgbdaagaae","bfefeaegdcdfdfbdcbg","abgcegbbdacdbdgfeffcegddgfgdebegbadfdafdeeccggcedddafdgfddcecgaeadcafeeaegffccdeecabfafacgaffcbgedbf","gcbbafcdcgaffbbgdaeebdfegeadcddaecbgdbbcfedbbdfebcdfcbegegddgceeebcga","cfageedbcdaegfcgeeb","acefcabadbfbd","eeebccfbeafcedeccafceegagabgeggafcebdfcacadcabebd","gdbbfdbebbaeafccgbffeccafeedabfefedbdffedbfbfcfgececdbaffcffefbdedacgdeefgbfbfegfcbfdebccgafbe","ggeabcabcfecbbbafcfaffgedefcdggedadedeaegcaedgbeggffbadgeaecfgbdadcegdagbffcgce","fdgfddcfecdagbaabdgaacbfebaaggadfecbedcfcdacdab","fdgbffcabefacdeggaacdgaacdgaadgcbacbbaaccebcdgagdbebecgdaefddagebcggdeeafagdbfegafafdaedcgagbbg","adbaedbcdfcefbeeabcgabdcbeaceggcccbcadfcegggfdcccdggfcgcfcdb","gagbgdeeedgcbfecefcdcfgbdaccbafegeeafgagaedfabafdbegafffgabcbfaedgebagdbdbeeffddaa","ffabagbafcceabfeeagbgcfcadfacfdfbeabdgebece","fdgbabgdbcggfebaaddabddfdfaefbdgfedbefcedffbfceaaddeabdgdfe","ddeffdadbccgedbbdagegbadcaegacfcedfeadcfffcdfdfeaab","dbcdbfcegaaebfceagaaccabegcdgcaddfcebgabdafccaccegcab","gddadcfagbgaceedfggegagbcgbefgcfbgabcccggdbgfeacgeabeedggbc","bbfge","cgcabdgfbfcgeceggeccdffgecccadecbgbgfgdbdedfdcagbf","caadffafbfcaacaegcddeeaaeaebdedffddgdbagbbbfgafdfacgadcddf","fadfdeffabfddfaeadafcfcfdcdfdcebbbbcfdbegac","bgcefdbefggddfcbcgbeceagccfbbeefcfca","eccbfbcfgeacbabdfcceddefdeadgaddacbfcccfgbafbbfeadgf","bgdcecdcdffegacbfbgegggcgbefacceffa","ecfbcaegebcfgddgfadadebfbbbdbeafababaaedgafbaafabf","eafgafdeefgaeagagbaaagcdfbbadbggbecabadeafcgfdfafedbdfaafbabgcaeebfcadgfcedffddb","efcfbdcfabbedggdbaddagebbbcgdfcggcagdfgedgeedfgfbcbcbdcfafbcdfbgdeeacfdagdgafcebdecdcaaggbcagfedg","gegfgfgcedgabfagdebbdgededaddaddfadgaebeaddfeaabbgdfgfcagdfffdfdbeg","eaafcfeggccgdabecgbggacffcabddfabcacgfcagbbgfcfeggcgfafdbffegddadagbbegbbedfagcbdabecabgegbcfcebadca","edbfddfdfeedfbagabdgdeffdeaeaad","bfdcfbgafbecac","gfbedgdbfcffdacbefacefaaaaebbfgfgcccaafaegcegag","abafafcefgcffcbbbecegcdcebaaggaefbc","fabcebeefabfbdbcbcdbeggeggccgeggbbcebbfeeagebgdaaeeadeadebefdcbeeagcafbgeaaegegedefefb","dfcacgaabcebcbgaadfedbcggcdd","bceafeddgbfebcgadcgeeeagdccdgdecfeddcaffeffeeaefgcdfa","aecaededfaacgcgabcbefegacdbcecea","fbd","fbcdggfccfecb","gecbgaffbbcbbfdccbaaf","ceaagcdcbeabggbgadeea","ccedgcbabefecfeddggffffccabfbdcbeggegfcbefegdbbdcfbcfgab","gfeggecgbaffdceffffbcgccgecggfefggf","cbfdbacbbegadfdddbgeggbccebeebfg","cedeggcaadbfdcdd","agdafbfaeddafcefabafgfagcdeadbfeadgfgafabbagbbedbbf","cadfcfdgafdgbcbeaebdcbabfcdfgda","bcgbdedbfbcddebbfccbbdcfdcfcbgcfacddeegfgb","afceccfadd","badcfddfefdgddbfaeggfedfddecdaaaccfaddbgdbgeaefddafdcd","fcbggfbfceebacebabefdegdefdbfecbgfdgbbggeacabbgaaafcdgabeaafdabdfafd"]
words = ["gjogbcjieghf","pipjmeocminhcjlnf","odpcnmanhgkbjfepfkbnkonlngcbnhhndcgf","lkekeelkafheinaedeil","ckhimemo","ocldikoadfoj","hjoapjfjgadopeiagekgaeohhkgnmhnmilbooeahoea","nehlkgnnjlcpgghbcddc","nechflpciekgapaeoleldpjmhbffemh","ikeipbakloff","djbllclieonhmglhcogabmohjhblimbpgcbomhlajcfgolj","gfedekeppjplebicnmgigkllclfmdlcaiiegijjbmaeenh","fcgppanpjbpfopflbn","oabbbjijlcgoealpeeihligbgkkfofpkajpgckamcicbhjki","bfjcaflkpocnihmchgnidfknglogdekekk","bgddlmmo","amm","npidnoinocifbcipbdnghnoipeepgemegbhelgoogkbjdklbgbi","bcgfhakpbihpagfjieomgb","imemniffba","mlmllfmdmgiiepongpnnjgimpfpegb","ejlfpigfmebfdihafjokbkegjepkmgbdbpjb","icgni","llfdlpkimbdnlifgedjbgmhbinckdfohaph","nlnfkgcalkipnj","amdljfmkofldjgn","hcpanadejodjll","fmaglnnlflofpdinkpdeheegkmd","modgebcm","dajopchpfdjippomfckhgjkfdap","hbhcocbgejba","jddaheifkopdnkjchbgmajcifo","hfbiboghoabclojgkfhenemoaaaapfmgplgpinmnmn","ljhamappmpoededabnfamcocal","ddpipllggbcf","cncpgimcdnccmdcebklhokkcalebjdafflmljglepn","jjahibo","flppeffoohhjpfjeiehdlecjceamjhpfjolh","gghjkonbnnc","anekhhpfhfpickaiemkbjlmcnblal","aoeaifcbceohdedcmnapndm","gplii","ncdgahmpnbaiocjnfbcfnlfcdjlo","cnaneieeeddhgpbhiohhomabflpfhkopl","pompfeacfedacfkocakc","glefjipgccnn","mloogiappgmoidddffmklpfchigeccehaajjahiehopnpckb","gaafanbaedeephnc","ndhgbfejpieddkemhfffpmnnaiomhcomppmjjnameeecc","hajjghlcemphjciipaoojf","adnnlpbnhibiicclgceednbghhkkfbbbdmjdfendbpgha","onjlbhcmfijeenhmjphffhiojkppibedaoaod","hhmkkajkghbghendpelgnchgbjepjflkfoilkpjpagle","aeicpnjkpdigpbibemc","ndnfmgfegeoojmnhkpdkmpfppepmknkkjdp","kmilgfbmeopalecklejndakenf","nomdfgaccegepjpjpci","ibjocmnkmhfcbebeoenofgbmced","jdbcgpclghlagbjjalmk","gnpppmaigiecpeanfbipikfjkmkgcd","ekincfljipkpnaigoepfglehkhcfjkilkddcgcaencfhdiamc","ejomebobpmkhnemiajlfoggkaknelmepjpdjlfgemidnlpjaie","mkkeobebpballljfgbbnojlcebennoakhjbpjojlcmhi","gobnhpjiekonpigdamdinlhoipcklihc","plfpbjddodclaepfeocfilopdkibnhkmkgiohcp","kmpj","bndfdkfhopdpgpdclmbolomgok","hljok","ikailfmbcoodo","lpmggpgbdoniekalfikmmmhfbjigfcglhdbpjkbe","eldc","pkogeobodngklcfpi","pigemleonfbgalekhpmndmg","bhaajhkbfpfigighgjm","olhoeegpncdcelcjfhbaipdj","hddcgjjkglhkmildook","hmdljkcnndollnne","kmocmldnolgefhdjejecalp","bckfekodcgcji","gjgignbijfnppjjmjcjkkfpd","migecfniddinljpglabanjpfd","lakbcombgmapjbkjkipajochmbgnnphmhgoggcba","lmjadbeofhejmp","epfcah","foccdafdmnln","fobfkcjdllldahb","apjodhnnlefdlnkkjifkgffmjhgdehbialgifbfdilhilfkfl","bmdfhpgmmoefccnaehpekgc","cfdolcoopofandhnhfdckk","bgnkcahcfklikliodldnngjogkkmojgcfjdfeehadmlealfia","ggohkhln","dgjflmmn","ihofhbhnadcfbecohcfgh","mhaghmbnghm","idgiihhliiahfdafokjdogniol","fgoncbagnoloa","ijoaaipplckkbjfmggjbgioloodecbnjgkakkmokah","hopjcdkckahjfdajikdihcfgankgddgmejbpikoelogokfgfd","bhoimklknekhkikmlodkchbngfpc","inijacbibbhbnlohicjajkihkpcbpnglpc","edgihonaffhjanafhkipaedlbldmnnepdmjjpgeblhfljgj","ebhcpkbahabgofl","bmakaci","fdlleihhkmpdhfedbbapbailippgh","fnpifbcedfaimfhhckkdaghgcofifgogeo","hlfkfa","pndnc","dcpabkojhpjimjfphkdldamglihagcbdij","lhlalgbplcppdcfamebnpg","paiijcbjmcjhiikmgepakagbemfaa","jcfbpbpabgabcfclhhajbgpblhohjeccieonjbohdihojjopdn","enompnginhjahlnbbajniacpnhpipmfpbhjdhkigajnpdcoodma","oeoikojkepokmbjddnmhamjlpjfamfdmhifnpcebnbpehda","pbhkpgkelfhckikefdcddjanhajdkolcilbjhlfo","ac","mijaecckeednhip","hkchjbekogbikjhpfadcpiplhcmdfdegahha","dliimlodfpkdhncl","mjhbo","pndnklljmegimihbdhongajngjiinapolcmbhobbjihbbogdlg","liodjllcnjdbpincfmahkam","nhiiemidgjdppajgidnmmaekakobhleegiihngcop","fbggfkenhnoihmjknda","hhhkkpfdehdpkocdjhkjkalbiajfflnapgagghbndcbiop","lgkplkkephinejokpeieoonaajplfchbkgghbjkjbjn","jiohachjnjdjkdiecmobkagna","dgoaenahcfhcmmpmeahgclbhopflagligoncncpadaoajn","fildimfejebi","cglhfio","peddphbkmbem","fcgbnhifpeecljkohfnhkfjffbilgnlhmmcekihg","mangehcpflcambi","phaonlljjdflljlaadifcoadiahpoikkmhad","dfdkdjnnnakiaebomhnkhbbjnmmdjehfkiiglpkmcdboahg","lhkflbidannjjadbjpfbbbhlpgbbpjlpp","iffmmhegphcpiglkjdllfe","mboimhokhdohekjaebdljcgomnnfppoec","ponmbiifhkhkognabhccdlgkdjifcejnlccfdilpdieomccng","bfdekngjaolfbelinjfolfaefgmfbdeobcceokcmeo","bijocmepoahm","hcpoamibgijakgeaegfmdelcijncpeebjkfjdg","lppeoefolopndaeeoopjhjejlhnncm","ofdogaboidlbakfhfkeh","ijfgmfkipdclgoedkpinigojlnlog"]
print(sol.maxProduct(words))