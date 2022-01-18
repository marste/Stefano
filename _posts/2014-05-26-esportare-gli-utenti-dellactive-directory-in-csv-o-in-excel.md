---
title: "Esportare gli utenti dell'active directory in .csv o in Excel"
author: Stefano Marzorati
layout: post
categories: [Windows]
---
<!-- HTML generated using hilite.me -->

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
  <pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">Dim</span> ObjWb 
<span style="color: #008800; font-weight: bold">Dim</span> ObjExcel 
<span style="color: #008800; font-weight: bold">Dim</span> x, zz 
<span style="color: #008800; font-weight: bold">Set</span> objRoot <span style="color: #333333">=</span> GetObject(<span style="background-color: #fff0f0">"LDAP://RootDSE"</span>) 
strDNC <span style="color: #333333">=</span> objRoot.Get(<span style="background-color: #fff0f0">"DefaultNamingContext"</span>) 
<span style="color: #008800; font-weight: bold">Set</span> objDomain <span style="color: #333333">=</span> GetObject(<span style="background-color: #fff0f0">"LDAP://"</span> <span style="color: #333333">&</span> strDNC) <span style="color: #888888">&#39; Bind to the top of the Domain using LDAP using ROotDSE </span>
<span style="color: #008800; font-weight: bold">Call</span> ExcelSetup(<span style="background-color: #fff0f0">"Foglio1"</span>) <span style="color: #888888">&#39; Sub to make Excel Document </span>
x <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">1</span> 
<span style="color: #008800; font-weight: bold">Call</span> enummembers(objDomain) 
<span style="color: #008800; font-weight: bold">Sub</span> <span style="color: #0066BB; font-weight: bold">enumMembers</span>(objDomain) 
<span style="color: #008800; font-weight: bold">On</span> <span style="color: #008800; font-weight: bold">Error</span> <span style="color: #008800; font-weight: bold">Resume</span> <span style="color: #008800; font-weight: bold">Next</span> 
<span style="color: #008800; font-weight: bold">Dim</span> Secondary(<span style="color: #0000DD; font-weight: bold">20</span>) <span style="color: #888888">&#39; Variable to store the Array of 2ndary email alias&#39;s </span>
<span style="color: #008800; font-weight: bold">For</span> <span style="color: #008800; font-weight: bold">Each</span> objMember <span style="color: #000000; font-weight: bold">In</span> objDomain <span style="color: #888888">&#39; go through the collection </span>

<span style="color: #008800; font-weight: bold">If</span> ObjMember.Class <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"user"</span> <span style="color: #008800; font-weight: bold">Then</span> <span style="color: #888888">&#39; if not User object, move on. </span>
x <span style="color: #333333">=</span> x <span style="color: #333333">+</span><span style="color: #0000DD; font-weight: bold">1</span> <span style="color: #888888">&#39; counter used to increment the cells in Excel </span>

objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">1</span>).Value <span style="color: #333333">=</span> objMember.Class 
<span style="color: #888888">&#39; I set AD properties to variables so if needed you could do Null checks or add if/then&#39;s to this code </span>
<span style="color: #888888">&#39; this was done so the script could be modified easier. </span>
SamAccountName <span style="color: #333333">=</span> ObjMember.samAccountName 
Cn <span style="color: #333333">=</span> ObjMember.CN 
FirstName <span style="color: #333333">=</span> objMember.GivenName 
LastName <span style="color: #333333">=</span> objMember.sn 
initials <span style="color: #333333">=</span> objMember.initials 
Descrip <span style="color: #333333">=</span> objMember.description 
Office <span style="color: #333333">=</span> objMember.physicalDeliveryOfficeName 
Telephone <span style="color: #333333">=</span> objMember.telephonenumber 
EmailAddr <span style="color: #333333">=</span> objMember.mail 
Fax <span style="color: #333333">=</span> objMember.facsimileTelephoneNumber 
Addr1 <span style="color: #333333">=</span> objMember.streetAddress 
City <span style="color: #333333">=</span> objMember.l 
State <span style="color: #333333">=</span> objMember.st 
ZipCode <span style="color: #333333">=</span> objMember.postalCode 
Title <span style="color: #333333">=</span> ObjMember.Title 
Department <span style="color: #333333">=</span> objMember.Department 
Company <span style="color: #333333">=</span> objMember.Company 
Manager <span style="color: #333333">=</span> ObjMember.Manager 
Profile <span style="color: #333333">=</span> objMember.profilePath 
LoginScript <span style="color: #333333">=</span> objMember.scriptpath 
HomeDirectory <span style="color: #333333">=</span> ObjMember.HomeDirectory 
HomeDrive <span style="color: #333333">=</span> ObjMember.homeDrive 
AdsPath <span style="color: #333333">=</span> Objmember.Adspath 
LastLogin <span style="color: #333333">=</span> objMember.LastLogin 

zz <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">1</span> <span style="color: #888888">&#39; Counter for array of 2ndary email addresses </span>
<span style="color: #008800; font-weight: bold">For</span> <span style="color: #008800; font-weight: bold">each</span> email <span style="color: #000000; font-weight: bold">in</span> ObjMember.proxyAddresses 
<span style="color: #008800; font-weight: bold">If</span> Left (email,<span style="color: #0000DD; font-weight: bold">5</span>) <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"SMTP:"</span> <span style="color: #008800; font-weight: bold">Then</span> 
Primary <span style="color: #333333">=</span> Mid (email,<span style="color: #0000DD; font-weight: bold">6</span>) <span style="color: #888888">&#39; if SMTP is all caps, then it&#39;s the Primary </span>
<span style="color: #008800; font-weight: bold">ElseIf</span> Left (email,<span style="color: #0000DD; font-weight: bold">5</span>) <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"smtp:"</span> <span style="color: #008800; font-weight: bold">Then</span> 
Secondary(zz) <span style="color: #333333">=</span> Mid (email,<span style="color: #0000DD; font-weight: bold">6</span>) <span style="color: #888888">&#39; load the list of 2ndary SMTP emails into Array. </span>
zz <span style="color: #333333">=</span> zz <span style="color: #333333">+</span> <span style="color: #0000DD; font-weight: bold">1</span> 
<span style="color: #008800; font-weight: bold">End</span> <span style="color: #008800; font-weight: bold">If</span> 
<span style="color: #008800; font-weight: bold">Next</span> 
<span style="color: #888888">&#39; Write the values to Excel, using the X counter to increment the rows. </span>

objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">2</span>).Value <span style="color: #333333">=</span> SamAccountName 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">3</span>).Value <span style="color: #333333">=</span> CN 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">4</span>).Value <span style="color: #333333">=</span> FirstName 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">5</span>).Value <span style="color: #333333">=</span> LastName 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">6</span>).Value <span style="color: #333333">=</span> Initials 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">7</span>).Value <span style="color: #333333">=</span> Descrip 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">8</span>).Value <span style="color: #333333">=</span> Office 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">9</span>).Value <span style="color: #333333">=</span> Telephone 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">10</span>).Value <span style="color: #333333">=</span> EmailAddr
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">11</span>).Value <span style="color: #333333">=</span> Fax 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">12</span>).Value <span style="color: #333333">=</span> Addr1 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">13</span>).Value <span style="color: #333333">=</span> City 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">14</span>).Value <span style="color: #333333">=</span> State 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">15</span>).Value <span style="color: #333333">=</span> ZipCode 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">16</span>).Value <span style="color: #333333">=</span> Title 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">17</span>).Value <span style="color: #333333">=</span> Department 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">18</span>).Value <span style="color: #333333">=</span> Company 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">19</span>).Value <span style="color: #333333">=</span> Manager 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">20</span>).Value <span style="color: #333333">=</span> Profile 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">21</span>).Value <span style="color: #333333">=</span> LoginScript 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">22</span>).Value <span style="color: #333333">=</span> HomeDirectory 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">23</span>).Value <span style="color: #333333">=</span> HomeDrive 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">24</span>).Value <span style="color: #333333">=</span> Adspath 
objwb.Cells(x, <span style="color: #0000DD; font-weight: bold">25</span>).Value <span style="color: #333333">=</span> LastLogin 
objwb.Cells(x,<span style="color: #0000DD; font-weight: bold">26</span>).Value <span style="color: #333333">=</span> Primary 

<span style="color: #888888">&#39; Write out the Array for the 2ndary email addresses. </span>
<span style="color: #008800; font-weight: bold">For</span> ll <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">1</span> <span style="color: #008800; font-weight: bold">To</span> <span style="color: #0000DD; font-weight: bold">20</span> 
objwb.Cells(x,<span style="color: #0000DD; font-weight: bold">26</span><span style="color: #333333">+</span>ll).Value <span style="color: #333333">=</span> Secondary(ll) 
<span style="color: #008800; font-weight: bold">Next</span> 
<span style="color: #888888">&#39; Blank out Variables in case the next object doesn&#39;t have a value for the property </span>
SamAccountName <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
Cn <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
FirstName <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
LastName <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
initials <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
Descrip <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
Office <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
Telephone <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
EmailAddr <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
Fax <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
Addr1 <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
City <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
State <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
ZipCode <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
Title <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
Department <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
Company <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
Manager <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
Profile <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
LoginScript <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
HomeDirectory <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
HomeDrive <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
Primary <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"-"</span> 
<span style="color: #008800; font-weight: bold">For</span> ll <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold">1</span> <span style="color: #008800; font-weight: bold">To</span> <span style="color: #0000DD; font-weight: bold">20</span> 
Secondary(ll) <span style="color: #333333">=</span> <span style="background-color: #fff0f0">""</span> 
<span style="color: #008800; font-weight: bold">Next</span> 
<span style="color: #008800; font-weight: bold">End</span> <span style="color: #008800; font-weight: bold">If</span> 

<span style="color: #888888">&#39; If the AD enumeration runs into an OU object, call the Sub again to itinerate </span>

<span style="color: #008800; font-weight: bold">If</span> objMember.Class <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"organizationalUnit"</span> <span style="color: #000000; font-weight: bold">or</span> OBjMember.Class <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"container"</span> <span style="color: #008800; font-weight: bold">Then</span> 
enumMembers (objMember) 
<span style="color: #008800; font-weight: bold">End</span> <span style="color: #008800; font-weight: bold">If</span> 
<span style="color: #008800; font-weight: bold">Next</span> 
<span style="color: #008800; font-weight: bold">End</span> <span style="color: #008800; font-weight: bold">Sub</span> 
<span style="color: #008800; font-weight: bold">Sub</span> <span style="color: #0066BB; font-weight: bold">ExcelSetup</span>(shtName) <span style="color: #888888">&#39; This sub creates an Excel worksheet and adds Column heads to the 1st row </span>
<span style="color: #008800; font-weight: bold">Set</span> objExcel <span style="color: #333333">=</span> CreateObject(<span style="background-color: #fff0f0">"Excel.Application"</span>) 
<span style="color: #008800; font-weight: bold">Set</span> objwb <span style="color: #333333">=</span> objExcel.Workbooks.Add 
<span style="color: #008800; font-weight: bold">Set</span> objwb <span style="color: #333333">=</span> objExcel.ActiveWorkbook.Worksheets(shtName) 
Objwb.Name <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Active Directory Users"</span> <span style="color: #888888">&#39; name the sheet </span>
objwb.Activate 
objExcel.Visible <span style="color: #333333">=</span> <span style="color: #008800; font-weight: bold">True</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">2</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"SamAccountName"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">3</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"CN"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">4</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"FirstName"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">5</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"LastName"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">6</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Initials"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">7</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Descrip"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">8</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Office"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">9</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Telephone"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">10</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Email"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">11</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Fax"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">12</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Addr1"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">13</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"City"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">14</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"State"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">15</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"ZipCode"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">16</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Title"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">17</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Department"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">18</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Company"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">19</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Manager"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">20</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Profile"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">21</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"LoginScript"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">22</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"HomeDirectory"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">23</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"HomeDrive"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">24</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Adspath"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">25</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"LastLogin"</span> 
objwb.Cells(<span style="color: #0000DD; font-weight: bold">1</span>, <span style="color: #0000DD; font-weight: bold">26</span>).Value <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"Primary SMTP"</span> 
<span style="color: #008800; font-weight: bold">End</span> <span style="color: #008800; font-weight: bold">Sub</span> 
MsgBox <span style="background-color: #fff0f0">"Fatto!"</span> <span style="color: #888888">&#39; show that script is complete</span>
</pre>
</div>

OPPURE

<!-- HTML generated using hilite.me -->

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
  <pre style="margin: 0; line-height: 125%"><span style="color: #008800; font-weight: bold">OPTION</span> EXPLICIT

<span style="color: #008800; font-weight: bold">dim</span> FileName, multivaluedsep,strAttributes
<span style="color: #008800; font-weight: bold">dim</span> strFilter, strRoot, strScope
<span style="color: #008800; font-weight: bold">dim</span> cmd, rs,cn
<span style="color: #008800; font-weight: bold">dim</span> objRoot, objFSO,objCSV
<span style="color: #008800; font-weight: bold">dim</span> comma, q, i, j, mvsep, strAttribute, strValue

<span style="color: #888888">&#39; ********************* Setup *********************</span>

<span style="color: #888888">&#39; The filename of the csv file produced by this script</span>
FileName <span style="color: #333333">=</span><span style="background-color: #fff0f0">"userexport.csv"</span>
<span style="color: #888888">&#39; Seperator used for multi-valued attributes</span>
multivaluedsep <span style="color: #333333">=</span> <span style="background-color: #fff0f0">";"</span>
<span style="color: #888888">&#39; comma seperated list of attributes to export</span>
strAttributes <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"GivenName,sn,initials,description,physicalDeliveryOfficeName,telephonenumber,mail,facsimileTelephoneNumber,streetAddress,l,st,postalCode,Title,Department,Company,Manager,profilePath,scriptpath,HomeDirectory,homeDrive,Adspath"</span>

<span style="color: #888888">&#39; Default filter for all user accounts (ammend if required)</span>
strFilter <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"(&(objectCategory=person)(objectClass=user))"</span>
<span style="color: #888888">&#39; scope of search (default is subtree - search all child OUs)</span>
strScope <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"subtree"</span>
<span style="color: #888888">&#39; search root. e.g. ou=MyUsers,dc=wisesoft,dc=co,dc=uk</span>
<span style="color: #888888">&#39; leave blank to search from domain root</span>
strRoot <span style="color: #333333">=</span> <span style="background-color: #fff0f0">""</span>

<span style="color: #888888">&#39; *************************************************</span>

q <span style="color: #333333">=</span> <span style="background-color: #fff0f0">""""</span>

<span style="color: #008800; font-weight: bold">set</span> cmd <span style="color: #333333">=</span> createobject(<span style="background-color: #fff0f0">"ADODB.Command"</span>)
<span style="color: #008800; font-weight: bold">set</span> cn <span style="color: #333333">=</span> createobject(<span style="background-color: #fff0f0">"ADODB.Connection"</span>)
<span style="color: #008800; font-weight: bold">set</span> rs <span style="color: #333333">=</span> createobject(<span style="background-color: #fff0f0">"ADODB.Recordset"</span>)

cn.open <span style="background-color: #fff0f0">"Provider=ADsDSOObject;"</span>
cmd.activeconnection <span style="color: #333333">=</span> cn

<span style="color: #008800; font-weight: bold">if</span> strRoot <span style="color: #333333">=</span> <span style="background-color: #fff0f0">""</span> <span style="color: #008800; font-weight: bold">then</span>
	<span style="color: #008800; font-weight: bold">set</span> objRoot <span style="color: #333333">=</span> getobject(<span style="background-color: #fff0f0">"LDAP://RootDSE"</span>)
	strRoot <span style="color: #333333">=</span> objRoot.get(<span style="background-color: #fff0f0">"defaultNamingContext"</span>) 
<span style="color: #008800; font-weight: bold">end</span> <span style="color: #008800; font-weight: bold">if</span>

cmd.commandtext <span style="color: #333333">=</span> <span style="background-color: #fff0f0">"&lt;LDAP://"</span> <span style="color: #333333">&</span> strRoot <span style="color: #333333">&</span> <span style="background-color: #fff0f0">"&gt;;"</span> <span style="color: #333333">&</span> strFilter <span style="color: #333333">&</span> <span style="background-color: #fff0f0">";"</span> <span style="color: #333333">&</span> _
		  strAttributes <span style="color: #333333">&</span> <span style="background-color: #fff0f0">";"</span> <span style="color: #333333">&</span> strScope

<span style="color: #888888">&#39;**** Bypass 1000 record limitation ****</span>
cmd.properties(<span style="background-color: #fff0f0">"page size"</span>)<span style="color: #333333">=</span><span style="color: #0000DD; font-weight: bold">1000</span>

<span style="color: #008800; font-weight: bold">set</span> rs <span style="color: #333333">=</span> cmd.execute
<span style="color: #008800; font-weight: bold">set</span> objFSO <span style="color: #333333">=</span> createobject(<span style="background-color: #fff0f0">"Scripting.FileSystemObject"</span>)
<span style="color: #008800; font-weight: bold">set</span> objCSV <span style="color: #333333">=</span> objFSO.createtextfile(FileName)

comma <span style="color: #333333">=</span> <span style="background-color: #fff0f0">""</span> <span style="color: #888888">&#39; first column does not require a preceding comma</span>
i <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold"></span> 

<span style="color: #888888">&#39; create a header row and count the number of attributes</span>
<span style="color: #008800; font-weight: bold">for</span> <span style="color: #008800; font-weight: bold">each</span> strAttribute <span style="color: #000000; font-weight: bold">in</span> SPLIT(strAttributes,<span style="background-color: #fff0f0">","</span>)
	objcsv.write(comma <span style="color: #333333">&</span> q <span style="color: #333333">&</span> strAttribute <span style="color: #333333">&</span> q)
	comma <span style="color: #333333">=</span> <span style="background-color: #fff0f0">","</span> <span style="color: #888888">&#39; all columns apart from the first column require a preceding comma</span>
	i <span style="color: #333333">=</span> i <span style="color: #333333">+</span> <span style="color: #0000DD; font-weight: bold">1</span>
<span style="color: #008800; font-weight: bold">next</span>

<span style="color: #888888">&#39; for each item returned by the Active Directory query</span>
<span style="color: #008800; font-weight: bold">while</span> rs.eof <span style="color: #333333">&lt;&gt;</span> <span style="color: #008800; font-weight: bold">true</span> <span style="color: #000000; font-weight: bold">and</span> rs.bof <span style="color: #333333">&lt;&gt;</span> <span style="color: #008800; font-weight: bold">true</span>
	comma<span style="color: #333333">=</span><span style="background-color: #fff0f0">""</span> <span style="color: #888888">&#39; first column does not require a preceding comma</span>
	objcsv.writeline <span style="color: #888888">&#39; Start a new line</span>
	<span style="color: #888888">&#39; For each column in the result set</span>
	<span style="color: #008800; font-weight: bold">for</span> j <span style="color: #333333">=</span> <span style="color: #0000DD; font-weight: bold"></span> <span style="color: #008800; font-weight: bold">to</span> (i <span style="color: #333333">-</span> <span style="color: #0000DD; font-weight: bold">1</span>)
		<span style="color: #008800; font-weight: bold">select</span> <span style="color: #008800; font-weight: bold">case</span> typename(rs(j).value)
		<span style="color: #008800; font-weight: bold">case</span> <span style="background-color: #fff0f0">"Null"</span> <span style="color: #888888">&#39; handle null value</span>
			objcsv.write(comma <span style="color: #333333">&</span> q <span style="color: #333333">&</span> q)
		<span style="color: #008800; font-weight: bold">case</span> <span style="background-color: #fff0f0">"Variant()"</span> <span style="color: #888888">&#39; multi-valued attribute</span>
			<span style="color: #888888">&#39; Multi-valued attributes will be seperated by value specified in</span>
			<span style="color: #888888">&#39; "multivaluedsep" variable</span>
			mvsep <span style="color: #333333">=</span> <span style="background-color: #fff0f0">""</span> <span style="color: #888888">&#39;No seperator required for first value</span>
			objcsv.write(comma <span style="color: #333333">&</span> q)
			<span style="color: #008800; font-weight: bold">for</span> <span style="color: #008800; font-weight: bold">each</span> strValue <span style="color: #000000; font-weight: bold">in</span> rs(j).Value
				<span style="color: #888888">&#39; Write value</span>
				<span style="color: #888888">&#39; single double quotes " are replaced by double double quotes ""</span>
				objcsv.write(mvsep <span style="color: #333333">&</span> replace(strValue,q,q <span style="color: #333333">&</span> q))
				mvsep <span style="color: #333333">=</span> multivaluedsep <span style="color: #888888">&#39; seperator used when more than one value returned</span>
			<span style="color: #008800; font-weight: bold">next</span>
			objcsv.write(q)
		<span style="color: #008800; font-weight: bold">case</span> <span style="color: #008800; font-weight: bold">else</span>
			<span style="color: #888888">&#39; Write value</span>
			<span style="color: #888888">&#39; single double quotes " are replaced by double double quotes ""</span>
			objcsv.write(comma <span style="color: #333333">&</span> q <span style="color: #333333">&</span> replace(rs(j).value,q,q <span style="color: #333333">&</span> q) <span style="color: #333333">&</span> q)
		<span style="color: #008800; font-weight: bold">end</span> <span style="color: #008800; font-weight: bold">select</span>
		
		comma <span style="color: #333333">=</span> <span style="background-color: #fff0f0">","</span> <span style="color: #888888">&#39; all columns apart from the first column require a preceding comma</span>
	<span style="color: #008800; font-weight: bold">next</span>
	rs.movenext
<span style="color: #008800; font-weight: bold">wend</span>

<span style="color: #888888">&#39; Close csv file and ADO connection</span>
cn.close
objCSV.Close

wscript.echo <span style="background-color: #fff0f0">"Finished"</span>
</pre>
</div>