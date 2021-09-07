# AI-conference-papers
The papers published in top-tier AI conferences in recent years.

## Conferences
| | AAAI | ICLR | CVPR | ICML | ICCV | ECCV | NIPS |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 2019 | [:heavy_check_mark:](paperlist/paperlist_aaai2019.tsv) | [:heavy_check_mark:](paperlist/paperlist_iclr2019.tsv) | [:heavy_check_mark:](paperlist/paperlist_cvpr2019.tsv) | [:heavy_check_mark:](paperlist/paperlist_icml2019.tsv) | [:heavy_check_mark:](paperlist/paperlist_iccv2019.tsv) | - | [:heavy_check_mark:](paperlist/paperlist_nips2019.tsv) |
| 2020 | [:heavy_check_mark:](paperlist/paperlist_aaai2020.tsv) | [:heavy_check_mark:](paperlist/paperlist_iclr2020.tsv) | [:heavy_check_mark:](paperlist/paperlist_cvpr2020.tsv) | [:heavy_check_mark:](paperlist/paperlist_icml2020.tsv) | - | [:heavy_check_mark:](paperlist/paperlist_eccv2020.tsv) | [:heavy_check_mark:](paperlist/paperlist_nips2020.tsv) |
| 2021 | [:heavy_check_mark:](paperlist/paperlist_aaai2021.tsv) | [:heavy_check_mark:](paperlist/paperlist_iclr2021.tsv) | [:heavy_check_mark:](paperlist/paperlist_cvpr2021.tsv) | [:heavy_check_mark:](paperlist/paperlist_icml2021.tsv) | TBU | - | TBU |

You can also see the [github page](https://creaiter.github.io/AI-conference-papers/).

## Search papers
You can perform the paper search like a following example:
```
python search.py -conf nips\|aaai -year \>\=2020 \<2021 -title quantiz\&prunin
```
The log of command execution:
```
16 tsv files are listed...
Finished to read all paper lists (19744 entries)...
Search conditions:
  - Conferences: nips|aaai
  - Years: >=2020 <2021
  - Title: quantiz&prunin
The searched 2 papers are saved at result_20210829-050022.tsv!
```
In the saved tsv file:
```
	Year	Conf	Title	Link	Authors	Keywords
0	2020	nips	Bayesian Bits: Unifying Quantization and Pruning	https://papers.nips.cc/paper/2020/hash/3f13cf4ddf6fc50c0d39a1d5aeb57dd8-Abstract.html	Mart van Baalen, Christos Louizos, Markus Nagel, Rana Ali Amjad, Ying Wang, Tijmen Blankevoort, Max Welling	-
1	2020	nips	Position-based Scaled Gradient for Model Quantization and Pruning	https://papers.nips.cc/paper/2020/hash/eb1e78328c46506b46a4ac4a1e378b91-Abstract.html	Jangho Kim, KiYoon Yoo, Nojun Kwak	-
```


## To do list
- [X] write a github page.
- [ ] crawl abstract texts.


## References
- [evanzd/ICLR2021-OpenReviewData](https://github.com/evanzd/ICLR2021-OpenReviewData)
