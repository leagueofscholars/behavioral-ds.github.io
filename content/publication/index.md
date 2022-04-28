---
type: "publication"
title: "Publications"
---

{{< loadbibtex >}}
<bibtex src="publications.bib"></bibtex>
<div style="margin-right: 10px; margin-top: -50px; float:right">
  <div class="input-group">
    <span class="input-group-addon"><i class="fa fa-search" style="padding-left: 5px;"></i></span>
    <input type="text" class="bibtex_search" id="searchbar" placeholder="Search publications">
  </div>
</div>
<div class="row">
  <div class="col-sm-12">
    <div id="bibtex_display" style="padding: 0 10px;"></div>
    <div class="bibtex_structure">
      <div class="group year" extra="DESC number">
        <div class="row">
          <div id="year-title" class="col-sm-12">
            <div class="title"></div>
          </div>
          <div class="col-sm-12">
            <div class="templates"></div>
          </div>
        </div>
      </div>
    </div>
    <div class="bibtex_template">
      <ul style="list-style-type:none">
        <li class="if author" style="font-weight: normal;">
          <b><span class="title"></span></b>,
          <span class="author"></span>,
          <span class="if booktitle">
            <span class="booktitle"></span>,
          </span>
          <span class="if journal">
            <span class="journal"></span>,
          </span>
          <span class="year"></span>
          <span class="if url" style="margin-left: 5px; font-size:16px">
            <a class="url" target="_blank">
              <i class="fas fa-link" style="color:black;"></i></a>
          </span>
          <span class="if url_paper" style="margin-left: 5px; font-size:16px">
            <a class="url_paper" target="_blank">
            <i class="fas fa-file-alt" style="color:black;"></i></a>
          </span>
          <span class="if url_code" style="margin-left: 5px; font-size:16px">
            <a class="url_code" target="_blank">
              <i class="fab fa-github" style="color:black;"></i></a>
          </span>
          <span class="if url_slides" style="margin-left: 5px; font-size:16px">
            <a class="url_slides" target="_blank">
              <i class="far fa-newspaper" style="color:black;"></i></a>
          </span>
          <span class="if url_video" style="margin-left: 5px; font-size:16px">
            <a class="url_video" target="_blank">
              <i class="fas fa-video" style="color:black;"></i></a>
          </spans>
          <span class="if abstract" style="margin-left: 5px;">
            <div class="morepage" >
              <span class="bibtexkey"></span>
              <span class="abstract noread"></span>
            </div>
          </span>
        </li>
      </ul>
    </div>
  </div>
</div>
