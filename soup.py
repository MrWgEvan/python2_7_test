# coding:utf-8

from bs4 import BeautifulSoup as bf


html=""" <a href="/341994" class="video-list-item-wrap" data-pdt-ele="0" data-id="341994">
                                        <div class="video-cover">
                      <img class="video-img video-img-lazy" data-original="https://i.h2.pdim.gs/90/0faab26e69a106392211d7cfab5b462d/w338/h190.webp" alt="道行之深非常人之所及">
                      <div class="video-overlay"></div>
                      <div class="video-play"></div>
                                            <div class="lottery-icon-list">
                                            </div>
                    </div>
                    <div class="video-info">
                      <span class="video-title" title="道行之深非常人之所及">道行之深非常人之所及</span>
                                            <span class="video-nickname" title="俄罗斯9527">
                                                <i class="icon-host-level icon-host-level-10" data-level="10"></i>
                                                俄罗斯9527                      </span>
                                            <span class="video-number">3.9万</span>
                      <span class="video-station-info">
                        <i class="video-station-num">21人</i>
                                               </span>
                    </div>"""

soupp = bf(html,"lxml")
users = soupp.select('span[class="video-nickname"]')[0].get_text().strip()
print users