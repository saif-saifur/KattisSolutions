<div class="book-container">
        <div id="bookmark" class="book-bookmark is-hidden">
            <div class="book-bookmark-text" data-cy="instruction-bookmark">
                View problem statement: <span class="book-bookmark-text-subtext">Add Two Numbers</span><i class="fas fa-chevron-left book-bookmark-text-icon"></i>
            </div>
        </div>
		    <div id="instructions-container" class="book-page-container grow book-page-fixed_width">
            <article class="book-page">
                <div class="book-page-fixed_width">
					          <div id="instructions-close" class="book-close"><i class="fas fa-chevron-left book-close-icon"></i>Hide</div>
                    <h1 class="book-page-heading">Add Two Numbers</h1>
                                            
  <div class="problembody">
    <p>In this problem, your program should read two whole numbers
    (also called integers) from the input, and print out their
    sum.</p>
    <p>As a refresher, here are some ways to read two numbers from
    standard input in a few different languages:</p>
    <pre># Python 3
line = input()
a, b = line.split()
a = int(a)
b = int(b)

// C++
// make sure to first "#include &lt;iostream&gt;"
int a, b;
std::cin &gt;&gt; a &gt;&gt; b;

// Java
// make sure to first "import java.util.Scanner;"
Scanner s = new Scanner(System.in);
int a = s.nextInt(), b = s.nextInt();
</pre>
    <h2>Input</h2>
    <p>The input contains one line, which has two integers
    <span class="tex2jax_process"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="0" style="font-size: 125.6%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi></math></mjx-assistive-mml></mjx-container></span> and <span class="tex2jax_process"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="1" style="font-size: 125.6%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>b</mi></math></mjx-assistive-mml></mjx-container></span>, separated by a single space. The
    bounds on these values are <span class="tex2jax_process"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="2" style="font-size: 125.6%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mstyle><mjx-mspace style="width: 0.167em;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>a</mi><mo>,</mo><mi>b</mi><mo>≤</mo><mn>1</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn><mstyle scriptlevel="0"><mspace width="0.167em"></mspace></mstyle><mn>000</mn></math></mjx-assistive-mml></mjx-container></span>.</p>
    <h2>Output</h2>
    <p>Output the sum of the two integers, <span class="tex2jax_process"><mjx-container class="MathJax CtxtMenu_Attached_0" jax="CHTML" tabindex="0" ctxtmenu_counter="3" style="font-size: 125.6%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44E TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2B"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="3"><mjx-c class="mjx-c1D44F TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>a</mi><mo>+</mo><mi>b</mi></math></mjx-assistive-mml></mjx-container></span>.</p>
    <table class="sample" summary="sample data">
      <tbody><tr>
        <th>Sample Input 1</th>
        <th>Sample Output 1</th>
      </tr>
      <tr>
        <td>
          <pre>3 4
</pre>
        <span class="copy-to-clipboard"></span></td>
        <td>
          <pre>7
</pre>
        <span class="copy-to-clipboard"></span></td>
      </tr>
    </tbody></table>
    <table class="sample" summary="sample data">
      <tbody><tr>
        <th>Sample Input 2</th>
        <th>Sample Output 2</th>
      </tr>
      <tr>
        <td>
          <pre>987 23
</pre>
        <span class="copy-to-clipboard"></span></td>
        <td>
          <pre>1010
</pre>
        <span class="copy-to-clipboard"></span></td>
      </tr>
    </tbody></table>
  </div>

                                    </div>
            </article>
        </div>

        <div id="editor-container" class="book-page-container grow static-fixed-parent is-dragging-unnaffected" data-problem-name="addtwonumbers" data-submit-url="/problems/addtwonumbers/submit" data-sourcelim="131072" data-may-submit="true" data-csrf-token="5186750808275354224705279157743650534883">
            <div id="edit-and-submit-tab" class="tab static-fixed-content pb-4 " style="width: 593px; position: fixed; min-height: auto; margin-top: 0px; height: calc(100vh - (var(--main-padding-y) * 2) - 0px);">
                <div class="l-strip_list-flex no-overflow">
                    <div class="strip-plain">
                        <nav class="tab-nav" data-mobile-select-classes="is-hidden@md tab-select-js"><a id="edit-and-submit-tab-link" class="tab-nav-item tab-nav-js active" title="Edit &amp; Submit" data-tab-id-to-open="edit-and-submit-tab" data-tab-id-to-close="edit-and-submit-tab">Edit &amp; Submit</a><a id="metadata-tab-link" class="tab-nav-item tab-nav-js " title="Metadata" data-tab-id-to-open="metadata-tab" data-tab-id-to-close="edit-and-submit-tab">Metadata</a><a id="submissions-tab-link" class="tab-nav-item tab-nav-js " title="Submissions" data-tab-id-to-open="submissions-tab" data-tab-id-to-close="edit-and-submit-tab">Submissions</a><div class="tabs-close book-close-tabs">Hide <i class="fas fa-chevron-right book-close-icon"></i></div></nav><select class="is-hidden@md tab-select-js" data-default-value="edit-and-submit-tab/edit-and-submit-tab"><option value="edit-and-submit-tab/edit-and-submit-tab" selected="selected">Edit &amp; Submit</option><option value="metadata-tab/edit-and-submit-tab">Metadata</option><option value="submissions-tab/edit-and-submit-tab">Submissions</option></select>
                    </div>
                                            <div id="editor-container-editor" class="editor-container-content is-hidden">
                            <div class="editor-top">
                                <div class="editor-top-header_items">
                                    <div class="editor-top-pages editor-top-header_item">
                                        <template id="editor-file_template">
                                            <div class="editor-top-input">
                                                <div role="textbox" contenteditable="true" class="editor-top-input-field" data-pageid="-1"></div>
                                                <i class="fas fa-times editor-top-input-remove" contenteditable="false"></i>
                                            </div>
                                        </template>
                                    </div>

                                    <div class="editor-top-header-options editor-top-header_item">
                                        <div class="editor-top-header-option">
                                            <select id="editor_languages_list" name="editor_languages_list" class="select2 editor-select2 select2-hidden-accessible" data-select2-id="select2-data-editor_languages_list" tabindex="-1" aria-hidden="true">
                                                <option value="" data-select2-id="select2-data-2-cc71"></option>
                                                
            <option data-defaultextension="c" data-defaultcode="" data-defaultname="addtwonumbers" value="C">
            C
        </option>
            <option data-defaultextension="cs" data-defaultcode="" data-defaultname="addtwonumbers" value="C#">
            C#
        </option>
            <option data-defaultextension="cpp" data-defaultcode="" data-defaultname="addtwonumbers" value="C++">
            C++
        </option>
            <option data-defaultextension="cob" data-defaultcode="" data-defaultname="addtwonumbers" value="COBOL">
            COBOL
        </option>
            <option data-defaultextension="lisp" data-defaultcode="" data-defaultname="addtwonumbers" value="Common Lisp">
            Common Lisp
        </option>
            <option data-defaultextension="fs" data-defaultcode="" data-defaultname="addtwonumbers" value="F#">
            F#
        </option>
            <option data-defaultextension="f90" data-defaultcode="" data-defaultname="addtwonumbers" value="Fortran">
            Fortran
        </option>
            <option data-defaultextension="go" data-defaultcode="" data-defaultname="addtwonumbers" value="Go">
            Go
        </option>
            <option data-defaultextension="hs" data-defaultcode="" data-defaultname="addtwonumbers" value="Haskell">
            Haskell
        </option>
            <option data-defaultextension="java" data-defaultcode="" data-defaultname="addtwonumbers" value="Java">
            Java
        </option>
            <option data-defaultextension="js" data-defaultcode="" data-defaultname="addtwonumbers" value="JavaScript (Node.js)">
            JavaScript (Node.js)
        </option>
            <option data-defaultextension="js" data-defaultcode="" data-defaultname="addtwonumbers" value="JavaScript (SpiderMonkey)">
            JavaScript (SpiderMonkey)
        </option>
            <option data-defaultextension="kt" data-defaultcode="" data-defaultname="addtwonumbers" value="Kotlin">
            Kotlin
        </option>
            <option data-defaultextension="m" data-defaultcode="" data-defaultname="addtwonumbers" value="Objective-C">
            Objective-C
        </option>
            <option data-defaultextension="ml" data-defaultcode="" data-defaultname="addtwonumbers" value="OCaml">
            OCaml
        </option>
            <option data-defaultextension="pas" data-defaultcode="" data-defaultname="addtwonumbers" value="Pascal">
            Pascal
        </option>
            <option data-defaultextension="php" data-defaultcode="" data-defaultname="addtwonumbers" value="PHP">
            PHP
        </option>
            <option data-defaultextension="pl" data-defaultcode="" data-defaultname="addtwonumbers" value="Prolog">
            Prolog
        </option>
            <option data-defaultextension="py" data-defaultcode="" data-defaultname="addtwonumbers" value="Python 2">
            Python 2
        </option>
            <option data-defaultextension="py" data-defaultcode="" data-defaultname="addtwonumbers" value="Python 3">
            Python 3
        </option>
            <option data-defaultextension="rb" data-defaultcode="" data-defaultname="addtwonumbers" value="Ruby">
            Ruby
        </option>
            <option data-defaultextension="rs" data-defaultcode="" data-defaultname="addtwonumbers" value="Rust">
            Rust
        </option>
    
                                            </select><span class="select2 select2-container select2-container--default" dir="ltr" data-select2-id="select2-data-1-ijql" style="width: 100%;"><span class="selection"><span class="select2-selection select2-selection--single" role="combobox" aria-haspopup="true" aria-expanded="false" tabindex="0" aria-disabled="false" aria-labelledby="select2-editor_languages_list-container" aria-controls="select2-editor_languages_list-container"><span class="select2-selection__rendered" id="select2-editor_languages_list-container" role="textbox" aria-readonly="true"></span><span class="select2-selection__arrow" role="presentation"><b role="presentation"></b></span></span></span><span class="dropdown-wrapper" aria-hidden="true"></span></span>
                                        </div>
                                        <div class="editor-top-header-option">
                                            <button id="editor-add_page-button" class="editor-top-button">+ New</button>
                                        </div>
                                        <div class="editor-top-header-option">
                                            <i class="fas fa-upload editor-top-icon editor-top-upload"><input type="file" class="editor-top-upload-input" multiple=""></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div id="editor" class=" ace_editor ace_hidpi ace-tm"><div style="position: absolute;"></div><textarea class="ace_text-input" wrap="off" autocorrect="off" autocapitalize="off" spellcheck="false" style="opacity: 0; font-size: 1px;"></textarea><div class="ace_gutter" aria-hidden="true"><div class="ace_layer ace_gutter-layer ace_folding-enabled" style="height: 1e+06px;"></div></div><div class="ace_scroller" style="line-height: 0px;"><div class="ace_content"><div class="ace_layer ace_print-margin-layer"><div class="ace_print-margin" style="left: 4px; visibility: visible;"></div></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_text-layer" style="height: 1e+06px; margin: 0px 4px;"></div><div class="ace_layer ace_marker-layer"></div><div class="ace_layer ace_cursor-layer ace_hidden-cursors"><div class="ace_cursor"></div></div></div></div><div class="ace_scrollbar ace_scrollbar-v" style="display: none; width: 20px;"><div class="ace_scrollbar-inner" style="width: 20px;">&nbsp;</div></div><div class="ace_scrollbar ace_scrollbar-h" style="display: none; height: 20px;"><div class="ace_scrollbar-inner" style="height: 20px;">&nbsp;</div></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: hidden;"><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;"></div><div style="height: auto; width: auto; top: 0px; left: 0px; visibility: hidden; position: absolute; white-space: pre; font: inherit; overflow: visible;">XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX</div></div></div>
                            <div class="editor-bottom">
                                <div id="mainclass-container" class="mainclass-container-content">
                                    <label for="mainclass" class="mainclass-label">Mainclass:</label>
                                    <input type="text" id="mainclass" class="mainclass-field">
                                </div>
                                <button id="submit_code_button" class="button button-primary button-medium button-small ml-auto">Submit</button>
                            </div>
                            <div class="editor-drag_highlight is-hidden">
                                <i class="fas fa-upload editor-container-intro-icon"></i>
                                Upload file(s)                            </div>
                        </div>

                        <div id="editor-container-intro" class="editor-container-content">
                            <div class="editor-container-intro-content">
                                <div class="editor-container-intro-half">
                                    <div class="editor-container-intro-half-content">
                                        <i class="fas fa-code editor-container-intro-icon"></i>
                                        <p class="editor-container-intro-text">
                                            Select your programming language of choice and start writing your code.                                        </p>
                                        <div class="editor-container-intro-select">
                                            <select id="intro_language_select" name="intro_languages_list" class="select2 intro-select2 select2-hidden-accessible" data-placeholder="Choose language" data-select2-id="select2-data-intro_language_select" tabindex="-1" aria-hidden="true">
                                                <option value=""></option>
                                                
            <option data-defaultextension="c" data-defaultcode="" data-defaultname="addtwonumbers" value="C">
            C
        </option>
            <option data-defaultextension="cs" data-defaultcode="" data-defaultname="addtwonumbers" value="C#">
            C#
        </option>
            <option data-defaultextension="cpp" data-defaultcode="" data-defaultname="addtwonumbers" value="C++">
            C++
        </option>
            <option data-defaultextension="cob" data-defaultcode="" data-defaultname="addtwonumbers" value="COBOL">
            COBOL
        </option>
            <option data-defaultextension="lisp" data-defaultcode="" data-defaultname="addtwonumbers" value="Common Lisp">
            Common Lisp
        </option>
            <option data-defaultextension="fs" data-defaultcode="" data-defaultname="addtwonumbers" value="F#">
            F#
        </option>
            <option data-defaultextension="f90" data-defaultcode="" data-defaultname="addtwonumbers" value="Fortran">
            Fortran
        </option>
            <option data-defaultextension="go" data-defaultcode="" data-defaultname="addtwonumbers" value="Go">
            Go
        </option>
            <option data-defaultextension="hs" data-defaultcode="" data-defaultname="addtwonumbers" value="Haskell">
            Haskell
        </option>
            <option data-defaultextension="java" data-defaultcode="" data-defaultname="addtwonumbers" value="Java">
            Java
        </option>
            <option data-defaultextension="js" data-defaultcode="" data-defaultname="addtwonumbers" value="JavaScript (Node.js)">
            JavaScript (Node.js)
        </option>
            <option data-defaultextension="js" data-defaultcode="" data-defaultname="addtwonumbers" value="JavaScript (SpiderMonkey)">
            JavaScript (SpiderMonkey)
        </option>
            <option data-defaultextension="kt" data-defaultcode="" data-defaultname="addtwonumbers" value="Kotlin">
            Kotlin
        </option>
            <option data-defaultextension="m" data-defaultcode="" data-defaultname="addtwonumbers" value="Objective-C">
            Objective-C
        </option>
            <option data-defaultextension="ml" data-defaultcode="" data-defaultname="addtwonumbers" value="OCaml">
            OCaml
        </option>
            <option data-defaultextension="pas" data-defaultcode="" data-defaultname="addtwonumbers" value="Pascal">
            Pascal
        </option>
            <option data-defaultextension="php" data-defaultcode="" data-defaultname="addtwonumbers" value="PHP">
            PHP
        </option>
            <option data-defaultextension="pl" data-defaultcode="" data-defaultname="addtwonumbers" value="Prolog">
            Prolog
        </option>
            <option data-defaultextension="py" data-defaultcode="" data-defaultname="addtwonumbers" value="Python 2">
            Python 2
        </option>
            <option data-defaultextension="py" data-defaultcode="" data-defaultname="addtwonumbers" value="Python 3" selected="" data-select2-id="select2-data-4-ugpp">
            Python 3
        </option>
            <option data-defaultextension="rb" data-defaultcode="" data-defaultname="addtwonumbers" value="Ruby">
            Ruby
        </option>
            <option data-defaultextension="rs" data-defaultcode="" data-defaultname="addtwonumbers" value="Rust">
            Rust
        </option>
    
                                            </select><span class="select2 select2-container select2-container--default" dir="ltr" data-select2-id="select2-data-3-h5eu" style="width: 100%;"><span class="selection"><span class="select2-selection select2-selection--single" role="combobox" aria-haspopup="true" aria-expanded="false" tabindex="0" aria-disabled="false" aria-labelledby="select2-intro_language_select-container" aria-controls="select2-intro_language_select-container"><span class="select2-selection__rendered" id="select2-intro_language_select-container" role="textbox" aria-readonly="true" title="
            Python 3
        ">
            Python 3
        </span><span class="select2-selection__arrow" role="presentation"><b role="presentation"></b></span></span></span><span class="dropdown-wrapper" aria-hidden="true"></span></span>
                                        </div>
                                        <button id="start_coding_button" class="button button-primary button-medium editor-container-intro-button">Start coding</button>
                                    </div>
                                </div>

                                <div class="editor-container-intro-half editor-container-intro-drop">
                                    <div class="editor-container-intro-half-content">
                                        <i class="fas fa-upload editor-container-intro-icon"></i>
                                        <p class="editor-container-intro-text">
                                            You can also upload your files by drag &amp; drop here or by browsing your computer.                                        </p>
                                        <button id="upload_files_button" class="button button-primary button-medium upload_files_button editor-container-intro-button">
                                            <input type="file" class="upload_files_button-input" multiple="">
                                            Upload files...                                        </button>
                                    </div>
                                    <div class="editor-drag_highlight is-hidden">
                                    </div>
                                </div>
                            </div>
                        </div>
                                    </div>
		        </div>
            <div id="metadata-tab" class="tab static-fixed-content static-fixed-content-no-expand pb-4 is-hidden" data-bookmark-label="Metadata" style="width: 593px; position: fixed; min-height: auto; margin-top: 0px;">
                <div class="l-strip_list-flex no-overflow">
                    <div class="strip-plain">
                        <nav class="tab-nav" data-mobile-select-classes="is-hidden@md tab-select-js"><a id="edit-and-submit-tab-link" class="tab-nav-item tab-nav-js " title="Edit &amp; Submit" data-tab-id-to-open="edit-and-submit-tab" data-tab-id-to-close="metadata-tab">Edit &amp; Submit</a><a id="metadata-tab-link" class="tab-nav-item tab-nav-js active" title="Metadata" data-tab-id-to-open="metadata-tab" data-tab-id-to-close="metadata-tab">Metadata</a><a id="submissions-tab-link" class="tab-nav-item tab-nav-js " title="Submissions" data-tab-id-to-open="submissions-tab" data-tab-id-to-close="metadata-tab">Submissions</a><div class="tabs-close book-close-tabs">Hide <i class="fas fa-chevron-right book-close-icon"></i></div></nav><select class="is-hidden@md tab-select-js" data-default-value="metadata-tab/metadata-tab"><option value="edit-and-submit-tab/metadata-tab">Edit &amp; Submit</option><option value="metadata-tab/metadata-tab" selected="selected">Metadata</option><option value="submissions-tab/metadata-tab">Submissions</option></select>
                    </div>
                    <div class="book-page">
                        <div class="metadata_list">
                                                            
    <div class="metadata_list-item">
        <span class="metadata_list-label">CPU Time limit</span>
        <span>1 second</span>
    </div>

                                
    <div class="metadata_list-item">
        <span class="metadata_list-label">Memory limit</span>
        <span>1024 MB</span>
    </div>

                            
                                                                                                
                                                                        
    <div class="metadata_list-item">
        <span class="metadata_list-label">Difficulty</span>
        <span><span class="difficulty_number difficulty_number-problems_table difficulty_easy">1.4</span>Easy</span>
    </div>

                                                                                                                        
    <div class="metadata_list-item">
        <span class="metadata_list-label">Statistics</span>
        <span><a href="/problems/addtwonumbers/statistics">Show</a></span>
    </div>

                                                                                        
    <div class="metadata_list-item">
        <span class="metadata_list-label">My Submissions</span>
        <span><a href="/users/saifur-rahman2/submissions/addtwonumbers">Show</a></span>
    </div>

                                                                                        <div class="metadata_list-item">
                                    <span class="metadata_list-label">Downloads</span>
                                    <div class="metadata_list-downloads">
                                                                                    <a href="/problems/addtwonumbers/file/statement/samples.zip" download="addtwonumbers.zip" }="">
                                                Sample data files
                                            </a>
                                                                            </div>
                                </div>
                                                        
                                                            <div class="metadata_list-item">
                                    <span class="metadata_list-label">Author</span>
                                    <div>
                                        <a href="/problem-authors/Greg%20Hamerly">Greg Hamerly</a>                                    </div>
                                </div>
                            
                                                                                            
    <div class="metadata_list-item">
        <span class="metadata_list-label">Source</span>
        <span>                                                                            <a href="/problem-sources/Kattis">Kattis</a>
                                                                    </span>
    </div>

                            
                                                                                            
    <div class="metadata_list-item">
        <span class="metadata_list-label">License</span>
        <span>                                                                            <a rel="license" href="https://creativecommons.org/licenses/by-sa/3.0/" style="vertical-align: middle;">
                                                                                                                <img class="problem-license" alt="Creative Commons License (cc by-sa)" src="https://licensebuttons.net/l/by-sa/3.0/80x15.png">
                                                                                                                </a>
                                                                    </span>
    </div>

                                                    </div>
                    </div>
                </div>
            </div>
            <div id="submissions-tab" class="tab static-fixed-content  pb-4 is-hidden" data-bookmark-label="Submissions" style="width: 593px; position: fixed; min-height: auto; margin-top: 0px; height: calc(100vh - (var(--main-padding-y) * 2) - 0px);">
                <div class="l-strip_list-flex no-overflow">
                    <div class="strip-plain">
                        <nav class="tab-nav" data-mobile-select-classes="is-hidden@md tab-select-js"><a id="edit-and-submit-tab-link" class="tab-nav-item tab-nav-js " title="Edit &amp; Submit" data-tab-id-to-open="edit-and-submit-tab" data-tab-id-to-close="submissions-tab">Edit &amp; Submit</a><a id="metadata-tab-link" class="tab-nav-item tab-nav-js " title="Metadata" data-tab-id-to-open="metadata-tab" data-tab-id-to-close="submissions-tab">Metadata</a><a id="submissions-tab-link" class="tab-nav-item tab-nav-js active" title="Submissions" data-tab-id-to-open="submissions-tab" data-tab-id-to-close="submissions-tab">Submissions</a><div class="tabs-close book-close-tabs">Hide <i class="fas fa-chevron-right book-close-icon"></i></div></nav><select class="is-hidden@md tab-select-js" data-default-value="submissions-tab/submissions-tab"><option value="edit-and-submit-tab/submissions-tab">Edit &amp; Submit</option><option value="metadata-tab/submissions-tab">Metadata</option><option value="submissions-tab/submissions-tab" selected="selected">Submissions</option></select>
                    </div>
                                            <section class="strip table-wrapper scrollable-container">
                                                        


<table class="table2 report_grid-problems_table double-rows" id="submissions"><thead><tr><th> </th> <th>Judgement</th> <th>Runtime</th> <th>Language</th> <th>Test cases</th> <th> </th> </tr></thead><thead></thead><tbody><tr data-submission-id="10345399"><td data-type="plagiarism" style="min-width:0px"></td><td data-type="status" style="min-width:160px"><div class="status is-status-accepted"><i class="fas fa-check status-icon is-accepted"></i>Accepted</div></td><td data-type="cpu" style="min-width:80px">0.05&nbsp;s</td><td data-type="lang" style="min-width:110px">Python 3</td><td data-type="testcases" style="min-width:80px"><div class="horizontal_item">16/16</div></td><td data-type="actions" style="min-width:130px"><a href="/submissions/10345399" class="button button-basic button-tightsmall">View Details</a></td></tr><tr class="testcases-row"><td></td><td colspan="5"><div class="status testcase testcase-row"><i class="fas fa-check status-icon is-accepted" title="Test case 1/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 2/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 3/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 4/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 5/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 6/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 7/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 8/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 9/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 10/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 11/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 12/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 13/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 14/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 15/16: Accepted"></i><i class="fas fa-check status-icon is-accepted" title="Test case 16/16: Accepted"></i></div></td></tr></tbody></table>                        </section>
                                    </div>
            </div>
			
        </div>
        <div id="bookmark-editor" class="book-bookmark is-hidden">
            <div class="book-bookmark-text" data-cy="editor-bookmark">
                Editor: <span id="editor-bookmark-label" class="book-bookmark-text-subtext" data-intro-text="Intro">Intro</span><i class="fas fa-chevron-right book-bookmark-text-icon"></i>
            </div>
        </div>
    </div>
