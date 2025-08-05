
# Plugin 'pyenv-virtualenv' for Windows

## Definition of Project

Python is my most favorite scripting language ever: 

![python_language_on_screen](./images/python_language_on_screen.png "Python Language on Screen")

But, in the development practice, latest after some months of frequently installing Python packages, you will find yourself in a severe problem: 

![python_virtualenv_requirements_problem](./images/python_virtualenv_requirements_problem.png "Multiple Projects Python Package Requirements Problem")

In Python, each project could have different requirements regarding the interpreter version and package versions.

Creating a Python virtual environment allows you to manage dependencies separately for different projects, preventing conflicts and maintaining cleaner setups.

With Python’s 'venv' module, you can create isolated environments that use different versions of libraries or Python itself. The product of this project guides you through creating, activating, and managing these environments efficiently.

But, using the Python 'venv' module efforts a lot of uneasy manual handling on command line.

This makes automation the order of the day.

To optimize configuring each Python project with virtual environment, you are recommended to use:
* A Python interpreter version management tool, e.g. 'pyenv' on Posix/Linux and Windows. 
  - A Python Virtual Environment management plugin, e.g. 'pyenv-virtualenv' on Posix/Linux only.

The goal of this project is to provide the missing 'pyenv-virtualenv' for Windows. 

## Architecture

Let's have a look on the software architecture and its dependencies of 'pyenv-virtualenv' for Windows. 

![pyenv-virtualenv_architecture](./images/pyenv-virtualenv_architecture.png "'pyenv-virtualenv' for Windows - Architecture'")

Thanks to the authors of 'pyenv' and 'pyenv-virtualenv'. Their documentation and the tools installed on Ubuntu Linux was very helpful to reverse engineer the 'pyenv-virtualenv' for Windows:
* <a href="https://github.com/kirankotari" rel="noopener noreferrer" target="_blank">Kiran Kumar Kotariy</a> and <a href="https://github.com/pyenv-win/pyenv-win/graphs/contributors/" rel="noopener noreferrer" target="_blank">Contributors</a>
* <a href="https://github.com/pyenv/pyenv-virtualenv" rel="noopener noreferrer" target="_blank">Yamashita, Yuu</a>

Opposite to 'pyenv', which depends on the Windows scripting languages only, the 'pyenv-virtualenv' for Windows depends on the Windows CMD/BAT scripting language (~1/3) and on the global Python version (~2/3) that is installed and configured via 'pyenv' for Windows.    

To fulfill the requirements for 'pyenv-virtualenv' for Windows, the global Python version must be 3.6+. Lower Python version are not supported. In addition, the Python package 'virtualenv' must be installed by pip into the global Python version.

Managed by 'pyenv-virtualenv' for Windows, for each project a single or multiple Python virtual environments can be installed and configured.

Within the path tree branch of the project, the local configured project properties define Python version and virtual environment name for the specific use case inside a project. 

These properties are inherited along the path tree branch. Using the 'activate' command without parameters, the specific virtual environment is automatically selected by 'pyenv-virtualenv' for Windows. 

The magic of 'pyenv-virtualenv' for Windows is located in the 'pyenv-win' command redirection feature. It activates the related utility scripts, which executable folders are prioritized within the PATH environment variable. Or, it automatically starts the python.exe or pip.exe in the related Python virtual environment 'Scripts' folder.

The result of this magic is an efficient and easy management of multiple projects on your development workstation, on test systems, productive servers or on the user client system in production.

## Project History

Up to June 2025, we have 'pyenv' for Posix (Linux, macOS, etc.) and Windows to manage the Python version for each project.

It has a plugin 'pyenv-virtualenv' for Posix (Linux, macOS, etc.), but it is not working under Windows.

Due to I develop my projects for Linux and Windows on a Windows workstation, I was missing the 'pyenv-virtualenv' plugin for Windows.

To immediately close this gap, I decided to analyze 'pyenv-virtualenv' and successfully passed a proof-on-concept milestone for 'pyenv-virtualenv' for Windows within a few hours.

I decided to begin the development end of June 2025.

This project is not a code/platform translation. From my point of view it would be too challenging to perform a painful code translation from Posix/Linux BASH to Windows CMD/BAT, due to the restrictions and failure risks of the Windows CMD/BAT script language. 

To bypass these hurdles, I reduced the CMD code to a minimum and used the Python version, I installed "Python 3.6+" using 'pyenv'. I set that version "global". Then I coded the complex and comprehensive scripts for the complete set of features for 'pyenv-virtualenv' for Windows in Python.

Because we have much more system resources in Windows 11, contrary to e.g. a tiny Raspberry Pi Zero on Linux platform, I was free to add some visual enhancements to this program:
* Doxygen HTML documentation 
* CLI Colors (ANSI) 
* CLI tables
* Comprehensive colored logging

This should help to learn and handle this complex command line utility collection much easier.

Now, after 14 days of development, I successfully passed the final comprehensive Alpha test for the new plugin of 'pyenv-virtualenv' for Windows. 

From my point of view, it completely works without any issues.

Now, in July 2025, I successfully finished developing this "pyenv" plugin, publishing it on GitHub and PyPI under:
~~~
pyenv-virtualenv-windows  
~~~

# Project Description

## Classification

This Open Source project and its documentation is not classified. 

Following to its license, it can be published and openly shared to the world.

## License

© 2025 Michael Paul Korthals. All rights reserved.

Published by Michael Paul Korthals in 2025 under GNU General Public License (GPL 3).

<details>
<summary>Contents of <code>LICENSE.txt</code></summary>

~~~
© 2025 Michael Paul Korthals. All rights reserved.
Published by Michael Paul Korthals in 2025 under GNU General Public License (GPL 3).

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

--- Appendix: GPL 3-----------------------------------------------------
 
                     GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

                       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.

  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.

  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

                     END OF TERMS AND CONDITIONS

            How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    <program>  Copyright (C) <year>  <name of author>
    This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type 'show c' for details.

The hypothetical commands 'show w' and 'show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<https://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>.

--- End of Document ----------------------------------------------------
~~~

</details>

## Redistribution Conditions

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

## Disclaimer

THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.

# User Manual

Know-how about command line interface (CLI) on Windows platform (CMD, Powershell, Cygwin) and the Python language are helpful to understand this user manual.

To learn about automated utilities this user manual describes, you should have in minimum a theoretical understanding what Python virtual environments are and how these work/behave. 

Otherwise, it would be wise to work through the "Google: python venv windows"-related Python docs and tutorials for first.

## Check Dependencies

> WARNING: Do not ignore this unit and read it carefully. There is no room for incompleteness. Otherwise, the dependencies are not completely fulfilled and you could fail.

Use the instructions on the <a href="https://github.com/pyenv-win/pyenv-win/" rel="noopener noreferrer" target="_blank">'pyenv' for Windows home page on GitHub</a> to completely install and configure 'pyenv'.   

Afterward, perform this manual test, to completely check the truth.

> NOTE: The conditions of this test will force you to call 'pyenv', 'python' or 'pip' with absolute file paths. This will bypass possible path conflicts, which will be resolved later during installation/docking of this plugin.    

Test schedule:
~~~{.cmd}
REM 1. Check if the 2 'pyenv' executable paths are included in the PATH.
path
REM 2. Check if the 'pyenv' Python executable is available.
where python
REM 3. Check if the 'pyenv' global Python version is correctly set.
{'pyenv'-related Python executable file path} -c "import sys; print(sys.executable); quit()"
REM 4. Ensure the actual versions of 'pip' and 'virtualenv' are installed.
{'pyenv'-related Python executable file path} -m pip install --upgrade pip virtualenv
~~~

Output (e.g.):
~~~
C:\Users\Paul>path
PATH=
...
C:\Users\Paul\.pyenv\pyenv-win\bin;C:\Users\Paul\.pyenv\pyenv-win\shims;
...

C:\Users\Paul>where python
C:\cygwin64\bin\python
C:\Program Files\KiCad\8.0\bin\python.exe
C:\Program Files\Inkscape\bin\python.exe
C:\Users\Paul\.pyenv\pyenv-win\shims\python
C:\Users\Paul\.pyenv\pyenv-win\shims\python.bat
C:\Users\Paul\AppData\Local\Microsoft\WindowsApps\python.exe

C:\Users\Paul>C:\Users\Paul\.pyenv\pyenv-win\shims\python -c "import sys; print(sys.executable); quit()"
C:\Users\Paul\.pyenv\pyenv-win\versions\3.12.10\python.exe

C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>C:\Users\Paul\.pyenv\pyenv-win\shims\python -m pip install --upgrade pip virtualenv
Requirement already satisfied: pip in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (25.1.1)
Requirement already satisfied: virtualenv in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (20.31.2)
Requirement already satisfied: distlib<1,>=0.3.7 in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from virtualenv) (0.3.9)
Requirement already satisfied: filelock<4,>=3.12.2 in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from virtualenv) (3.18.0)
Requirement already satisfied: platformdirs<5,>=3.9.1 in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from virtualenv) (4.3.8)
~~~

> WARNING: If there is only the slightest deviation, it is essential you reconfigure 'pyenv'. Otherwise, the plugin 'pyenv-virtualenv' installer or the plugin itself will cancel after running into error messages.

Let's have a detailed view on the resulting output and possible remediation tasks.

1. Existence of two 'pyenv' executable paths in PATH environment variable:
~~~
C:\Users\Paul>path
PATH=
...
C:\Users\Paul\.pyenv\pyenv-win\bin;C:\Users\Paul\.pyenv\pyenv-win\shims;
...
~~~
* In case of success: 
  * The two 'pyenv'-related paths are included PATH.
  * Both paths are beginning with '%USERPROFILE%\\.pyenv\\pyenv-win'.
  * The first path ends with '\\bin'.
  * The second path ends with '\\shims'.
* In case of failure/deviation:
  * Install/configure 'pyenv' for Windows on your computer.
  * Repeat test 1.

2. Existence of the 'python' command in the call priority list called by 'where python':
~~~
C:\Users\Paul>where python
C:\cygwin64\bin\python
C:\Program Files\KiCad\8.0\bin\python.exe
C:\Program Files\Inkscape\bin\python.exe
C:\Users\Paul\.pyenv\pyenv-win\shims\python
C:\Users\Paul\.pyenv\pyenv-win\shims\python.bat
C:\Users\Paul\AppData\Local\Microsoft\WindowsApps\python.exe
~~~
* In case of success:
  * Python executable is found in directory '%USERPROFILE%\\.pyenv\\pyenv-win\\shims'
* In case of failure/deviation:
  * Jump back to the detailed remediation instructions in test 1.
  * Repeat test 1 and 2.

3. Global 'pyenv' global version configuration for Python:
~~~
C:\Users\Paul>C:\Users\Paul\.pyenv\pyenv-win\shims\python -c "import sys; print(sys.executable); quit()"
C:\Users\Paul\.pyenv\pyenv-win\versions\3.12.10\python.exe
~~~
* In case of success:
  * Python found its interpreter executable as '%USERPROFILE%\\.pyenv\\pyenv-win\\versions\\{global version number}\\python.exe'.
* In case of failure/deviation:
  * Call 'pyenv install {global version number}'.
  * Call 'pyenv global {global version number}'.
  * Call 'pyenv versions' to check, which version is '*' global.
  * Repeat test 3. 

4. Packages 'pip' and 'virtualenv' are up-to-date in the 'pyenv' global Python version:
~~~
C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>C:\Users\Paul\.pyenv\pyenv-win\shims\python -m pip install --upgrade pip virtualenv
Requirement already satisfied: pip in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (25.1.1)
Requirement already satisfied: virtualenv in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (20.31.2)
Requirement already satisfied: distlib<1,>=0.3.7 in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from virtualenv) (0.3.9)
Requirement already satisfied: filelock<4,>=3.12.2 in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from virtualenv) (3.18.0)
Requirement already satisfied: platformdirs<5,>=3.9.1 in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from virtualenv) (4.3.8)
~~~
* In case of success:
  * The requirements for 'pip' and 'virtualenv' and its dependencies are completely satisfied.
* In case of failure/deviation:
  * Ensure that the global Python version in 'pyenv' is 3.6 or higher.
  * Repeat the whole test sequence beginning with test 1.

If everything is crystal-clear fine, then step forward to the next unit.

## Installation

This package contains no importable code. Instead, it transports a command-line-based tool that docks a plugin to the previously installed 'pyenv' toolset.

Hardware and system software requirements are the same as for 'pyenv' for Windows.

This plugin additionally depends on 'pyenv' with globally installed Python version '3.6' or higher.

This plugin will be installed with Python 'pip'.

> IMPORTANT NOTE: Installing the plug-in, you could be forced to call 'pyenv', 'python' or 'pip' with absolute file paths. This will bypass possible path conflicts, which will be resolved during this installation/docking of this plugin. Use the 'where' command to uniquely identify the absolute paths to the 'pyenv'-related executables.

~~~{.cmd}
where pip
pip install pyenv-virtualenv-windows
~~~

Display the package properties:
~~~{.cmd}
pip show pyenv-virtualenv-windows
~~~
Identify the location of the package from output:
~~~
C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>pip show pyenv-virtualenv-windows
Name: pyenv-virtualenv-windows
Version: 1.2.5
Summary: ...
Home-page: ...
Author: ...
Author-email: ...
License-Expression: ...
Location: C:\Users\Paul\.pyenv\pyenv-win\versions\3.12.10\Lib\site-packages
Requires: virtualenv ...
Required-by: ...
~~~

In this example the combined {Location Path} is, e.g.:
~~~
C:\Users\Paul\.pyenv\pyenv-win\versions\3.12.10\Lib\site-packages\pyenv-virtualenv-windows
~~~

Dock 'pyenv-virtualenv' for Windows as a plugin to 'pyenv' for Windows. To do this, you must run the following three commands in a console terminal:

~~~{.cmd} 
cd {Location Path}
dir
install.bat
~~~

> NOTE: If you need to run the 'install.bat' automatically without user interaction, you must run the calling automation script/shell as 'Administrator'.  

If the docking runs without showing error messages and returns error level zero, then the docking of this plugin has been successful.

## Path Conflicts

> IMPORTANT NOTE: If the docking fails because existing PATH Conflicts then read this unit carefully.

> My personal opinion: 'Conflicts don't exist to create more conflict, more emotional pressure, or more physical violence. They exist only for a brief moment, until you embark on the adventure to resolve them with maximum efficiency and sustainability, given the circumstances.'

Let's go to work:

Windows has two PATH environment variables:
1. The 'Machine' PATH.
2. The 'User' PATH.

The program 'install.bat' for 'pyenv-virtualenv for Windows e.g. calls the audit script 'install_audit.ps1', which is written in Windows PowerShell. Its task is to detect possible problems in the PATH prioritization, which could jeopardize 'pyenv' Python calls. These are the PATH conflicts.

PATH conflicts arise, because 'pyenv' is installed in the 'User' PATH by default. However, if programs that offer Python were previously or later installed in the 'Machine' PATH for all users, they will intercept the Python call. This is because the 'Machine' PATH has higher priority than the 'User' PATH.

When the 'install.bat' for 'pyenv-virtualenv' for Windows is failing through PATH conflicts, then you have 3 'pyenv'-related PATH items at the beginning of the 'User' PATH environment variable:
~~~
%USERPROFILE%\.pyenv\pyenv-win\plugins\pyenv-virtualenv\shims
%USERPROFILE%\.pyenv\pyenv-win\bin
%USERPROFILE%\.pyenv\pyenv-win\shims
~~~
The first path has been set by the plugin 'pyenv-virtualenv' for Windows. This PATH item must be the first of all.
The following two paths has been set by 'pyenv' for Windows.    

These PATH items must have the highest priority to call Python from console terminal or command line interface. Otherwise, 'pyenv' and its dependent 'pyenv-virtualenv' for Windows will fail. 

As I have done this for the first time on my developer workstation, the installer found 3 'Path Conflicts'. E.g.:
~~~
> install.bat
...
ERROR   Found path conflicts (RC = 1):
ERROR     * C:\cygwin64\bin
ERROR     * C:\Program Files\KiCad\8.0\bin
ERROR     * C:\Program Files\Inkscape\bin
...

> where python
C:\cygwin64\bin\python
C:\Program Files\KiCad\8.0\bin\python.exe
C:\Program Files\Inkscape\bin\python.exe
C:\Users\Paul\.pyenv\pyenv-win\shims\python
C:\Users\Paul\.pyenv\pyenv-win\shims\python.bat
C:\Users\Paul\AppData\Local\Microsoft\WindowsApps\python.exe
C:\Program Files\KiCad\bin\python.exe
~~~
Here we have 3 conflicting Python calls before it is the turn for 'pyenv'.  

I solved the 3 conflicts by elevating the 'pyenv' PATH items including its plugin to serve "For All Users".

Nevertheless, it is your decision how you manage your path priorities according to your needs.

It could be possible to automate this, but for security reasons and the lack of predictability of all possible use cases around the world, I would rather leave this complex PATH definition in your capable hands.

The bad news is, this is very complex, but it is a good training for newcomers to go deeper into the complexity of the workings of PATH environment variable.  

The good news is, that this effort must be only be done once in most cases.

So, it is your choice, to SELECT ONE OF THE 2 WAYS to solve this problem:

1. Manually move the three 'pyenv'-related path items from the beginning of the 'User' PATH environment variable to the BEGINNING of the 'Machine' PATH:
  * This will enable 'pyenv' to for 'All Users'.
  * On your computer you need 'Administrator' privileges to change the 'Machine' PATH.
  * Recursively change the security properties of the '%USERPROFILE%\\.pyenv' folder tree: 
    * For selected named users with read only permissions (using Python versions and virtual environments unchanged.
    * For selected users with read/write permissions (manging Python versions virtual environments and packages).
    * Inform and train your team members in detail, how to use Python on this computer.
  * IN DETAIL (for newcomers, learning how to master more complex Windows PATH definition): 
    * Go to Windows 'Settings' and find 'path'.
    * Select '~edit environment variables'. 
    * Press the '~Environment Variables ..." button to open the relevant dialog.
    * Edit the 'User' PATH as string. Not as list.
    * Cut the three 'pyenv'-related path items from the beginning of 'User' PATH into clipboard.
    * Ensure the quality of the PATH string: 
      * Delete spaces around the ';' item separators.
      * Replace each ';;' by ';'.
      * Delete ';' at beginning and end of the PATH string. 
    * Submit the new 'User' PATH.
    * Edit the 'Machine' PATH as string. Not as list.
    * Set the cursor at the beginning of the 'Machine' PATH, unselecting the PATH string.  
    * Paste the clipboard and additionally insert a ';' path separator. 
    * Ensure the quality of the PATH string: 
      * Delete spaces around the ';' item separators.
      * Replace each ';;' by ';'.
      * Delete ';' at beginning and end of the PATH string. 
    * Submit the new 'Machine' PATH.
    * Submit all other open dialogs in this context with 'OK'.

2. Manually move the conflicting Python-providing application-related path items from 'Machine' PATH to 'User' PATH, AFTER the three 'pyenv'-related path items.
  * This will degrade the other Python-providing applications for 'This User Only'.
  * On your computer you need 'Administrator' privileges to change the 'Machine' PATH.
  * IN DETAIL (for newcomers, learning how to master more complex Windows PATH definition):
    * Go to Windows 'Settings' and find 'path'.
    * Select '~edit environment variables'. 
    * Press the '~Environment Variables ..." button to open the relevant dialog.
    * Edit the 'Machine' PATH as text. Not as list.
    * Copy the complete 'Machine' into clipboard.
    * Paste the clipboard into a first empty document on your text editor.
    * Indentify the conflicting application path items in the first document 
    * Cut each identified path item and paste it into the second empty document.
    * Organize the PATH string in both documents each in a single row.
    * Ensure the quality of the PATH strings: 
      * Delete spaces around the ';' item separators.
      * Replace each ';;' by ';'.
      * Delete ';' item separator at beginning and end of each PATH string. 
    * Copy the new 'Machine' PATH string from the first document into the clipboard.
    * Edit the 'Machine' PATH as text. Not as list.
    * Delete the whole content of the 'Machine' PATH edit field.
    * Paste the clipboard.
    * Submit the new 'Machine' PATH.
    * Copy the new 'User' PATH string from the second document into the clipboard.
    * Edit the 'User' PATH as text. Not as list.
    * Set the cursor right the last 'pyenv'-related PATH item,
    * Paste the clipboard.
    * Insert a ';' separator if needed.
    * Ensure the quality of the PATH string: 
      * Delete spaces around the ';' item separators.
      * Replace each ';;' by ';'.
      * Delete ';' item separator at beginning and end of PATH string. 
    * Submit the new 'User' PATH.
    * Submit all other open dialogs in this context with 'OK'.

FINALLY: 
  * Close and reopen the console terminal to let the changes take effect.
  * Use these commands to check if everything should work according to your needs:
    * 'path'
    * 'where python'  

OPTIONAL:
  * Changes in the PATH could affect all command line-based Python programs you have on your computer. 
  * E.g. if you are starting elevated Python programs by the Windows task scheduler:
    * Immediately configure 'pyenv-virtualenv'-managed Python virtual environments for these programs.
    * Manage the package requirements for these Python virtual environments.
    * Adopt the program launcher commands in the Task scheduler to activate and deactivate the related Python virtual environments.  
    * Restart the computer to test these programs.
    * Check (e.g. in the logs) if everything is working as you expect.

## Location

To find all 'pyenv' locations, execute the following command:
~~~{.cmd}
REM If Cygwin is not installed and configured:
set 
echo Search for "PYENV" manually.
REM Having Cygwin on board:
set | grep "pyenv"
~~~
Output (e.g.):
~~~
path=C:\Users\Paul\.pyenv\pyenv-win\bin;C:\Users\Paul\.pyenv\pyenv-win\shims; ...
PYENV=C:\Users\Paul\.pyenv\pyenv-win\
PYENV_HOME=C:\Users\Paul\.pyenv\pyenv-win\
PYENV_ROOT=C:\Users\Paul\.pyenv\pyenv-win\
~~~

This tree chart gives an overview about the most important sub-folders in this plugin:
~~~
%PYENV_ROOT%\plugins\pyenv-virtualenv
├───bin
├───docs
│   ├───html
│   └───images
├───libexec
└───shims
~~~

> NOTE: After a successful installation and docking, the complete Doxygen Industry Standard Documentation is available in the 'docs\\html' folder.

Use this command to open the Doxygen Industry Standard Documentation:
~~~{.cmd}
"%PYENV_ROOT%plugins\pyenv-virtualenv\docs\html\index.html"
~~~

## Usage

### Concepts

For better understanding, how 'pyenv-virtualenv' for Windows is working, read this unit carefully, before you start to use 'pyenv-virtualenv'. 

#### Audits

Each utility in 'pyenv-virtualenv' for Windows is auditing your system environment to avoid functional problems or lack of completeness in installing/configuring 'pyenv' and 'pyenv-virtualenv' for Windows. 

In case of deviation, the utility logs a red-colored error message and a remediation instruction to the console. Afterward, the program will be canceled to avoid further problems.

It is essential that you remediate all deviations to finally get 'pyenv-virtualenv' for Windows working well.

If everything is fine, nothing will be logged about the audits.

If you want to see the audit activities and its results on detail on the console terminal, execute these commands:
~~~{.cmd}
REM Set log level to "verbose"
set LOG_LEVEL=15
REM Execute a passive utility, which shows information only
pyenv virtualenvs
REM Reset log level to default ("info")
set LOG_LEVEL=20
~~~

#### Commands

The management of Python versions and virtual environments for Posix/Linux and Windows is implemented as a series of commands, which are executed in the CLI terminal. 

In both platform ecosystems the syntax and behavior of the utilities are nearly identical. 'pyenv-virtualenv' for Windows includes some new enhancements. Use the '-h' or '--help' argument to display the details for each utility command.

Using Python virtual environment, the short form 'venv' has been established within the publications of the developer community. Also, 'venv' is quicker and easier to type in opposite to 'virtualenv'.

In addition, in Windows the words 'new' and 'list' are more familiar to create and to list somthing on command line. 

"rm" in Cygwin, Posix/Linux operating systems and "del" on Windows are the common synonyms to delete/remove something in both ecosystems. 

To round this up, 'activate' and 'deactivate' are the known commands to enable/disable the Python virtual environment.   

To take these mods into account, these short and alternative command names are implemented:

| Original                | Short             | Alternative     |
|:------------------------|:------------------|:----------------|
| pyenv virtualenv        | -                 | pyenv venv-new  |
| pyenv virtualenvs       | -                 | pyenv venv-list |
| pyenv virtualenv-delete | pyenv venv-del    | venv-rm         |
| pyenv virtualenv-prefix | pyenv venv-prefix | -               |
| pyenv virtualenv-props  | pyenv venv-props  | -               |
| pyenv activate          | -                 | activate        |
| pyenv deactivate        | -                 | deactivate      |

Now the best of the two worlds can coexist. Use this as you like.

My favorite and more coherent command list for 'pyenv-virtualenv' for Windows is:

| Command          | Description                                                |
|:-----------------|:-----------------------------------------------------------|
| pyenv venv-new   | Create a new virtual environment.                          |
| pyenv venv-list  | List Python versions, environments and project properties. |
| pyenv venv-del   | Delete a virtual environment.                              |
| pyenv venv-props | Manage project properties.                                 |
| activate         | Activate virtual environment.                              |
| deactivate       | Deactivate virtual environment.                            |

#### Project Properties

To control, which Python version and virtual environment are in use for a specific local project, some hidden information files can be managed:

| File Name       | Content                                                                                                       |
|:----------------|:--------------------------------------------------------------------------------------------------------------|
| .python-version | 3-Digit Python version number (e.g. 3.12.10)                                                                  |
| .python-env     | Virtual environment short name (e.g. cinema_5)                                                                |
| .tree-excludes  | Tuple of folder names to exclude from local project tree view.<br/>E.g.: ('docs', '\_\_pycache\_\_', '.idea') |

These files automatically inherit the version, virtual environment and exclude settings along the Windows directory paths.

These settings allow you to use different Python versions and virtual environments within the same project.

The content of '.tree-excludes' file allows to exclude 'spam' folders from the tree view. E.g. 'docs', caches and IDE project configuration folders. The excludes prevents you from scrolling through non-relevant information. 

In this example project, the setup routine and the application are using the same Python version, but different virtual environments:
~~~
C:\Users\Paul\eclipse\cinema_5
│   .python-version  <-- Configured Python version  
│   docs.doxyfile  
├───back-end
│   .python-env      <-- Configured virtual environment
│   .tree-excludes   <-- Configured directory tree excludes
│   back-end.bat     <-- Launcher to automate app call
│   back-end.py      <-- Application script
├───docs
│   └───images
└───setup
    .python-env      <-- Configured another virtual environment
    setup.bat        <-- Launcher to automate the setup call
    setup.py         <-- Setup script
~~~

#### Help

Each of the tool scripts includes Python argument parser 'argparse'. If you add the '-h' or '--help' option:  
~~~{.cmd}
pyenv virtualenv --help 
~~~

See output of this call for details:
~~~
Usage: pyenv virtualenv [-h] [-v] [-p | --props | --no-props ] [version] [name]

Create a version-assigned and named Python virtual environment in "pyenv".

Positional arguments (which can be omitted):
  [version]             Python version, which must be already installed in 
                        "pyenv". Default: The global Python version.
  [name]                Short name of the new Python virtual environment.

Options:
  -h, --help            Show this help message and exit.
  -p, --props, --no-props
                        Add the files `.python-version` and `.python-env` 
                        as project properties to CWD. Default: --no_props.
  -v, --version         Display the version number of this "pyenv-virtualenv" 
                        release and ignore all other arguments.
~~~

#### Logging

Each of the 'pyenv' scripts has a colored comprehensive logging implemented. 

> NOTE: No log files are implemented. The log output is written to console only:

The logging is divided into to the following log levels:

| Level    | Value | Color   | Description                                              |
|:---------|------:|:--------|:---------------------------------------------------------|
| critical |    50 | red+    | Critical error, which let the program exit immediately.  |
| error    |    40 | red     | Normal error message, which finishes the program.        |
| success  |    35 | green   | Success message.                                         |
| warning  |    30 | yellow  | Warning message.                                         |
| notice   |    25 | magenta | Notice message.                                          |
| info     |    20 | white   | Information message (Default level).                     |
| verbose  |    15 | blue    | Verbose message for overview in diagnosis.               |
| debug    |    10 | green   | Debug message to trace states in running the program.    |
| spam     |     5 | gray    | Mass messages for loop observations and deep diagnosis.  |

The lower the log level is, much more colored log will appear on console terminal. 

The log level can be set using the OS environment variable "LOG_LEVEL":
~~~{.cmd}
REM Set log level to "debug"
set LOG_LEVEL=10
REM Override virtual environment
pyenv virtualenv 3.12 cinema_5 --props
REM Reset loglevel to default
set LOG_LEVEL=20
~~~

Output:

![pyenv_virtualenv_debug_logging](./images/pyenv_virtualenv_debug_logging.png "Colored Comprehensive Logging")

### Create Virtual Environment

To generate a virtual environment for the Python version installed in 'pyenv', call
'pyenv virtualenv', specifying the installed Python version you want and the name
of the virtualenv directory (e.g. the short name of your project folder). 

In addition, this script configures the version and the virtual environment for your project.

#### Create with Version and Name

> NOTE: Be aware that this command copies 2 hidden files into your project folder. These files are your 'pyenv virtualenv' project properties, which contain the Python version number and the virtual environment name. If required, other scripts in thi sworkflow read these files to know which Python version and virtual environment is set.

This example creates a virtual environment named 'cinema_5', which depends on version 'Python 3.12.10':
~~~{.sh}
REM Change directory to your Python project folder
cd "%USERPROFILE%\eclipse-workspace\cinema_5"
REM Generate the virtual environment and set project properties in CWD
pyenv virtualenv 3.12.10 cinema_5 --props
REM Show project property files
dir .python*.*
type .python-version
type .python-env
~~~

Output:
~~~
INFO     Creating Python virtual environment in "pyenv":
INFO       * Version: 3.12.10
INFO       * Name:    cinema_5
INFO       * Set project properties: True
INFO     This will take some seconds ...
SUCCESS  Virtual environment "cinema_5" is installed in "pyenv", depending on "Python 3.12.10".

 Datenträger in Laufwerk C: ist SYSTEM
 Volumeseriennummer: 38E4-3A30

 Verzeichnis von C:\Users\Paul\eclipse-workspace\cinema_5

Fr, 04. 07. 2025  07:46                 8 .python-env
Fr, 04. 07. 2025  07:46                 7 .python-version
               2 Datei(en),             15 Bytes
               0 Verzeichnis(se), 117.726.687.232 Bytes frei
3.12.10
cinema_5
~~~

'pyenv virtualenv' forwards 2 positional arguments and 1 option to the underlying command that actually creates the virtual environment using 'python -m venv':

This will create a virtual environment based on 'Python 3.12.10' under '%PYENV_ROOT%/versions' in a folder junction called 'cinema_5-3.12.10'.

That folder junction is linked to folder:
~~~
%PYENV_ROOT%/versions/3.12.10/envs/cinema_5-3.12.10
~~~
Finally, the 'pyenv virtualenv' project property files has been written.

#### Create With Name Only

If there is only one positional argument given to 'pyenv virtualenv', the virtualenv will be created with the given name based on the current pyenv Python version.

~~~{.cmd}
REM Check global Python version 
pyenv version
3.12.10 (set by ...)
REM Change directory to your Python project folder
cd "%USERPROFILE%\eclipse-workspace\cinema_5"
REM Generate the virtual environment and set project properties
pyenv virtualenv 3.12.10 cinema_5 --props
~~~

Output:
~~~
3.12.10 (set by ...)

INFO     Creating Python virtual environment in "pyenv":
INFO       * Version: 3.12.10 (global)
INFO       * Name:    cinema_5
INFO       * Set project properties: True
INFO     This will take some seconds ...
SUCCESS  Virtual environment "cinema_5" is installed in "pyenv", depending on "Python 3.12.10".
~~~

### List Installed Virtual Environments

The utility 'pyenv virtualenvs' displays 3 tables and a tree view:
1. Installed Python Versions
2. Available Virtual Environments
3. Local Project Properties
4. Optional (if using '-t' or '--tree' option): CWD tree view

Output:

![pyenv_virtualenvs_tables](./images/pyenv_virtualenvs_tables.png "") ![pyenv_virtualenvs_tree](./images/pyenv_virtualenvs_tree.png "Data Listing")

If you know about Python Virtual Environment it is easy for you to interpret the data. Some stati are depending on the PWD path, the Python version numbers and the installed and globalized versions and virtual environments.

There are two entries for each virtualenv, and the shorter one is just a symlink.

### Activate Virtual Environment

> NOTE: The behavior of the 'activate' command depends on the project property settings on CWD. See unit 'Concepts' / 'Project Properties'.

Use these commands to activate and use the configured virtual environment:
~~~{.cmd}
REM Activate Python virtual environment
activate
... use and manage the virtual environment ...
REM Deactivate Python virtual environment
deactivate
~~~

![pyenv-virtualenv_activate](./images/pyenv-virtualenv_activate.png "Activated Virtual Environment")

Please notice the details in the screenshot above:
* The 'activate' command opens the virtual environment. It adds information in colors to the terminal prompt:
  - Virtual environment name (yellow) 
  - Python version number (cyan)
  - Path string (blue)
* The successful activation is proved by checking the output 'sys.executable' in Python.
* The 'deactivate' command removes virtual environment name and version from terminal prompt.
* After finally executed the 'deactivate' command, it closes the virtual environment. The color of the path in the terminal prompt turns to white again.

To ensure interoperability the equivalent Posix/Linux commands are available in Windows. Here the complete command listing with all synonyms and argument scenarios: 
~~~{.cmd}
pyenv activate
pyenv activate <name>
pyenv activate <version> <name>
pyenv deactivate
activate
activate <name>
activate <version> <name>
deactivate
~~~

### Delete Installed Virtual Environment

Manually removing the related junction (symbolic links) in the 'versions' directory and the related virtual environment in the 'envs' subfolder of that version will delete a virtual directory.

See in these folders:
~~~
%PYENV_ROOT%versions
%PYENV_ROOT%versions\{version}\envs
~~~

To automate this, use the 'pyenv-virtualenv' plugin to uninstall virtual environments:
~~~{.cmd}
pyenv virtualenv-delete {version} {name}
pyenv virtualenv-delete 3.12.10 cinema_5a
~~~

> NOTE: This will only delete the virtual environment, so called 'cinema_5a'. The version '3.12.10' remains untouched. 

Use 'pyenv' as usual to manage the Python versions and to uninstall these:
~~~{.cmd}
REM Uninstall
pyenv uninstall {version}
pyenv uninstall 3.9.6
REM Set version 'global'
pyenv global {version}
pyenv global 3.13.3
~~~

Finally, to check your results in a single view, call:
~~~{.cmd}
pyenv virtualenvs
~~~

### Manage Project Properties

This utility manages two virtual environment-related project properties:
1. .python-version (e.g. 3.12.10)  
2. .python-env (cinema_5)

It has 3 features:

| Command                       | Description                        | Feature Aliases            |
|:------------------------------|:-----------------------------------|:---------------------------|
| pyenv virtualenv-props set    | Set project properties in CWD.     | s                          |
| pyenv virtualenv-props unlink | Unlink project properties in CWD.  | u,d,del,delete,r,rm,remove |
| pyenv virtualenv-props list   | List project properties in CWD. *) | l,ls                       |

\*\) Optional (using 't' or '--tree argument) display CWD tree view.


![pyenv-virtualenv_activate](./images/pyenv_virtualenv-props.png "Project Properties List")

#### Exclude 'Spam' Folders 

In 'pyenv-virtualenv' for Windows an additional project property '.tree-excludes' is implemented. This property will also be automatically inherited to its subfolders. 

It is used to exclude 'spam' folders from files and folders tree-view, which is displayed by the 'pyenv virtualenvs' and 'pyenv virtualenv-props list' commands.

It can be manually managed in CWD as follows:
~~~{.cmd}
REM Set the '.tree-exclude' property in CWD, e.g.:
echo ('docs', '__pycache__', '.idea') > .tree-excludes
REM Edit the '.tree-exclude' property in CWD, e.g.:
notepad++ .tree-exclude 
REM Unlink the '.tree-exclude' property from CWD, e.g.:
del .tree-excludes
REM List the project properties incl. the CWD tree, e.g.:
pyenv virtualenv-props list --tree
~~~

### Virtual Environment Prefix

Use these commands to get the path prefix for virtual environment:
~~~{.cmd}
REM Get prefix for the CWD
pyenv virtualenv-prefix
REM Get prefix for installed virtual environment
pyenv virtualenv-prefix {name}
pyenv virtualenv-prefix cinema_5a 
~~~

Output: 

![pyenv-virtualenv-prefix](./images/pyenv-virtualenv-prefix.png "Virtual Environment Prefix")

### Reconfigure After 'pyenv' Upgrade

After upgrading "pyenv" some path settings and the patch could be reconfigured. This ensures that the 'pyenv-virtualenv' plugin continues working without errors.

In case of problems following to a 'pyenv' update/upgrade or as preventive measure, simply repeat the installation of 'pyenv-virtualenv' for Windows. See complete details in unit 'Installation'. 

## Python Venv

There is a [venv](http://docs.python.org/3/library/venv.html) module available for 'Python 3.3+'.

It provides an executable module 'venv', which is the successor of 'virtualenv' and distributed by default.

'pyenv-virtualenv' uses 'python -m venv' if it is available and the 'virtualenv' command is not available.

Each utility in 'pyenv-virtualenv' tries to import the 'virtualenv' near the beginning of the program. This let the utility programs exit immediately by error and so should avoid problems with globalized outdated Python versions. 

## Error Diagnosis

> IMPORTANT NOTE: When discussing a functional issue with me on GitHub, words means nearly nothing. Always support your bug descriptions with console terminal output.

To support effective error diagnosis, e.g. use the following commands.

The resulting information can be analyzed in case of a problem on your systems. It gives detailed hints about what could be wrong.

To try, copy one of these commands or all commands and paste these into a console terminal:
~~~{.cmd}
REM 1. Check 'pyenv':
echo %PYENV_ROOT%
where pyenv

REM 2. Show list of Python executables in priority order:
where python
where pip

REM 3. Show PATH environment variable in the actuial console terminal:
path

REM 4. Show python version
python --version 

REM 5. Show loaded Python packages:
pip freeze

REM 6. Show only the first 30 lines of the 'systeminfo' output excluding 
REM confidential network data ('head' only works if ~'Cygwin' is on board).
systeminfo | head -30
~~~

If you have this information and have studied the documentation, then in most cases you should know how to solve the problem. Otherwise, you are welcome to contribute an issue, to solve it.

[![github](https://img.shields.io/badge/GitHub-Pyenv%20Virtualenv%20Windows%20|%201.2-2040A0)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows)
[![github](https://img.shields.io/badge/GitHub-Pyenv%20Windows%20|%201.2-4080C0)](https://github.com/pyenv-win/pyenv-win/)

> NOTE: Before reporting an issue, you should be aware of the commands associated with the 'pyenv' or 'pyenv-virtualenv' tools. These have different maintainers and are provided by different sites. Create your issue on the relevant site.

# Operations Manual

This unit describes the operation of this plugin.

Knowledge about administration of Windows operating systems, Windows command line interface (CMD and PS) and Python handling are essentially required to understand this documentation.

## Tooling

The following Open Source tools are strongly recommended to fulfill the requirements of this and other software projects.

### Markdown (.MD) Editor

In this project, I used PyCharm to edit the project documentation supporting documents (e.g.: 'README.md', 'PYPI_README.md).

It deprecated and replaced the formerly used tool 'Ghostwriter' completely.

### Doxygen

Doxygen is a widely-used documentation generator tool in software development. <a href="https://www.doxygen.nl" rel="noopener noreferrer" target="_blank">Download.</a>

It automates the generation of documentation from source code comments, parsing information about classes, functions, and variables to produce output in formats like HTML and PDF. By simplifying and standardizing the documentation process, Doxygen enhances collaboration and maintenance across diverse programming languages and project scales.

In this project, I used Doxygen to document the project and all its assets.

#### Documentation

<a href="https://www.doxygen.nl/manual/" rel="noopener noreferrer" target="_blank">Doxygen Documentation</a> 

### Windows Command Line Script

The windows command line scripting is still part of the Windows 11 Operating system since the beginning of Microsoft MS-DOS at the dawn of the information age in the 1980s.

In this project ist is used to implement a lot of launcher batch files, operative routines and to help compiling and opening the documentation.

The advantage of command line script is, that it need not any dependencies to run on Windows 11.

#### Documentation

  * <a href="https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands" rel="noopener noreferrer" target="_blank">Windows Command Line Script Documentation</a>

  * <a href="https://www.tutorialspoint.com/batch_script/" rel="noopener noreferrer" target="_blank"> Windows Command Line Script Tutorial</a>

### Windows PowerShell

PowerShell is the modern, powerful and object-oriented command line script language in Windows.

In this project, it is used by 'pyenv' for Windows to install that tool on a 'fresh' Windows system without any other software installed.

The advantage of PowerShell is, that it need not any dependencies to run on Windows 11.

#### Documentation

  * <a href="https://https://learn.microsoft.com/en-us/powershell/" rel="noopener noreferrer" target="_blank">Windows PowerShell Documentation</a>

  * <a href="https://www.tutorialspoint.com/powershell/" rel="noopener noreferrer" target="_blank"> Windows PowerShell Tutorial</a>

### Cygwin

A large collection of GNU and Open Source tools, which provide functionality similar to a Linux distribution on Windows. <a href="https://www.cygwin.com/" rel="noopener noreferrer" target="_blank">Download.</a>

In this project I used Cygwin to extend the Windows command line language. E.g.:
  * grep
  * ls
  * tee
  * cat
 
#### Documentation

<a href="https://www.cygwin.com/" rel="noopener noreferrer" target="_blank">Cygwin Documentation</a>

### Python

Python is a programming language that lets you work more quickly and integrate your systems more effectively. You can learn to use Python and see almost immediate gains in productivity and lower maintenance costs. <a href="https://www.python.org/downloads/" rel="noopener noreferrer" target="_blank">Download.</a>

In this project, it gave the basis for the more comprehensive scripts, which design is too challenging to implement in CMD/BAT.

#### Documentation

<a href="https://www.python.org/doc/" rel="noopener noreferrer" target="_blank">Python Documentation</a>

### PyCharm Community Edition

PyCharm is an integrated development environment (IDE) from the Czech company JetBrains for the Python programming language.

There is a free, open source community version and a professional version. The community version can be used to create pure Python projects.  
<a href="https://www.python.org/downloads/" rel="noopener noreferrer" target="_blank">Download.</a>

In this project, PyCharm is used as IDE to edit code files not only for Python, but for other destinations too.

It allows to debug Python code files and helps the developer to avoid all kinds of program errors. This rises the quality of the code and reduce the test efforts.

Under Debian Linux you install this IDE using the command line interface. See:

<a href="https://www.jetbrains.com/help/pycharm/installation-guide.html#f00dd51b" rel="noopener noreferrer" target="_blank">PyCharm Installation Guide</a>

![pycharm_ide_python](./images/pycharm_ide.png "PyCharm IDE")

PyCharm is healthy. It allows dark mode, TAB indents and soft wraps.

#### Configuration

1. Go to Menu / Settings / Appearance & Behavior / Appearance find the 'Theme' item and set it to 'Dark'.
2. Go to Menu / Settings / Editor / Code Style / Python / Tabs & Indents and set to use TAB as indent.
3. Go to Menu / Settings / Editor / General, find "soft wraps" and set the file list for all your code file types.

Recommended file types for soft wrapping in this project are:
~~~
*.md; *.txt; *.rst; *.adoc; *.py; *.conf; *.json; *.yaml; *.yml; *.bat; *.cmd; *.ps1; *.js; *.html; *.htm; *.php
~~~

#### File and Code Templates for Fram

To avoid obsolete recurring workload, it is a good idea to use templates.

PyCharm supports 2 kinds of templates:
  * Code templates (Live Templates) to insert and configure recurring code snippet.
  * File templates to create and configure the skeleton of a code file.

For the Fram framework custom live templates for PyCharm are available in the project folder:
~~~
# Code Templates
'.\fram\codeTemplates\_ fram.xml'
# File Templates
'.\fram\fileTemplates\*.*'
~~~

In Windows import/export that files into the settings folder of the current PyCharm version e.g.:
~~~
# Code Templates
%APPDATA%\JetBrains\PyCharmCE2025.1\templates
# File Templates
%APPDATA%\JetBrains\PyCharmCE2025.1\fileTemplates
~~~

> NOTE: The Live Templates (code templates) must be enabled explicitly in 'File and Code Templates' section of the PyCharm settings.

Afterward, restart the PyCharm IDE to make the code templates available pressing Ctrl-J.

The file templates are registered in PyCharm and selectable when creating a new file. 

Press Ctrl-Alt-S and find 'template' to edit the templates.

#### Documentation

<a href="https://www.jetbrains.com/help/pycharm/getting-started.html" rel="noopener noreferrer" target="_blank">PyCharm Documentation</a>

### Notepad++

The best practice open source Editor for small projects is the free community version of "Notepad++" for Windows. <a href="https://notepad-plus-plus.org/downloads/" rel="noopener noreferrer" target="_blank">Download</a>.

Under Debian Linux you install this editor using the command line interface:
~~~{.sh}
sudo -i
apt update && upgrade -y
snap install notepad-plus-plus
exit
~~~

Notepad++ accelerates and excels the development of web applications and scripts by these features:
  * Healthy dark theme
  * Project tree viewer
  * Shell script editor
    * Colored code 
    * Smart and detailed text completion for Python code
    * Spellchecker
  * Markdown editor (for Doxygen main page, GitHub, etc.)
    * Colored code
    * Spellchecker
  * Textfile editor
  * ... and much more

In this project, I used Notepad++ to analyze data files, log files, scripts and code changes.

![notepad++_php](./images/notepad++_php.png "Notepad++ Editor")

Notepad++ is healthy. It allows dark mode, TAB indents and soft wraps.

#### Configuration

1. Go to Menu / Settings / Preferences / Dark Mode and select the 'Dark mode'.
2. Go to Menu / Settings / Style Configurator / and select e.g. the theme "Obsidian".
3. Go to Menu / Settings / Preferences / Indentation set to use TAB as indent and 'Indent size' to 4.
4. Go to Menu / View / Word wrap. Toggle this menu item to switch word wrapping on or off. 

#### Documentation

<a href="https://notepad-plus-plus.org/online-help/" rel="noopener noreferrer" target="_blank">Notepad++ Documentation</a>

### GIMP Graphic Editor

GIMP is a high quality framework for scripted image manipulation, with multi-language support such as C, C++, Perl, Python, Scheme, and more. <a href="https://www.gimp.org/" rel="noopener noreferrer" target="_blank">Download</a>.

In this project, I used the GIMP Graphic Editor to edit the multi-layer photo of the DUNE CD-ROM on dark background.

#### Documentation

<a href="https://www.gimp.org/tutorials/" rel="noopener noreferrer" target="_blank">GIMP Graphic Editor Documentation</a>

### 7-ZIP Archiver

7-Zip is a free Open Source file archiver with a high compression ratio. <a href="https://www.7-zip.org/download.html" rel="noopener noreferrer" target="_blank">Download</a>.

Main features:
* High compression ratio in 7z format with LZMA and LZMA2 compression
* Supported formats:
  * Packing / unpacking: 7z, XZ, BZIP2, GZIP, TAR, ZIP and WIM
  * Unpacking only: APFS, AR, ARJ, CAB, CHM, CPIO, CramFS, DMG, EXT, FAT, GPT, HFS, IHEX, ISO, LZH, LZMA, MBR, MSI, NSIS, NTFS, QCOW2, RAR, RPM, SquashFS, UDF, UEFI, VDI, VHD, VHDX, VMDK, XAR and Z.
* For ZIP and GZIP formats, 7-Zip provides a compression ratio that is 2-10 % better than the ratio provided by PKZip and WinZip
* Strong AES-256 encryption in 7z and ZIP formats
* Self-extracting capability for 7z format
* Integration with Windows Shell
* Powerful File Manager
* Powerful command line version
* Plugin for FAR Manager
* Localizations for 87 languages

7-Zip works in Linux, macOS, Windows 11 / 10 / 8 / 7 / Vista / XP / 2022 / 2019 / 2016 / 2012 / 2008 / 2003 / 2000.

In this project I use 7-Zip on command line to compress its Doxygen Industry Standard Documentation into a ZIP file, which is further on publish on GitHub. Users can download the ZIP File, unpack it and then view the documentation in a Web Browser.

### Documentation

<a href="https://www.7-zip.org/" rel="noopener noreferrer" target="_blank">7-Zip Documentation</a>

## Documentation

Documentation is an essential part of the software development process.

### Advantages

In documenting, you often get a first feedback about, what you are just developing. This feedback rises the efficiency of your development and reduces the amount of test efforts.

Your working techniques are important to reproduce your things and methods by other persons, or by yourself if you have to rework this project after a long period of inactivity.

### Language

The primary technical documentation language is English. Depending on legal requirements, other languages could be necessary e.g. if a product is sold in non-English speaking countries or cultures.

If English is not your first language, be aware that any type of AI translator is not able to understand complex correlations. Avoid falling into the AI quality trap. Instead, develop your language from good literature and communicating with people.

> NOTE: To rise the quality of your documentation, install and activate the Spell Check Plugin, which shows the typos by underlining it e.g. in red.

### Security & Legal

This project is shared to the world.

So, data protection is an important issue.

> NOTE: All confidential and personal information, especially those in screenshots and photos of the author and related persons, data and assets must be wiped out before parts of this documentation will be published.

> NOTE: The content of published documentation must not either violate the rules and legal regulation applied in the context of its publication, nor, it must not uncover the author's common activities for any kind of profiling, tracking and stalking.

### Tooling

The industry standard documentation tool is <a href="https://www.doxygen.nl/" rel="noopener noreferrer" target="_blank">Doxygen</a>. It is available for Linux, Mac and Windows. <a href="https://www.doxygen.nl/" rel="noopener noreferrer" target="_blank">Doxygen</a>.

As off 2022, Doxygen is healthy from my point of view. It produces a dark mode web interface per default. Don't use older versions anymore, which write on unhealthy white background.

### Other Documentation

In parallel to this documentation other documentation are relevant for this project:

  * <a href="https://www.doxygen.nl/manual/" rel="noopener noreferrer" target="_blank">Doxygen Manual</a> 
  * <a href="https://www.markdownguide.org/" rel="noopener noreferrer" target="_blank">Markdown Documentation</a> 
  * <a href="https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands" rel="noopener noreferrer" target="_blank">Windows Command Line Script Documentation</a>
  * <a href="https://www.tutorialspoint.com/batch_script/" rel="noopener noreferrer" target="_blank"> Windows Command Line Script Tutorial</a>
  * <a href="https://learn.microsoft.com/en-us/powershell/" rel="noopener noreferrer" target="_blank">Windows PowerShell Documentation</a>
  * <a href="https://www.tutorialspoint.com/powershell/" rel="noopener noreferrer" target="_blank"> Windows PowerShell Tutorial</a>
  * <a href="https://www.cygwin.com/" rel="noopener noreferrer" target="_blank">Cygwin Documentation</a>
  * <a href="https://www.python.org/doc/" rel="noopener noreferrer" target="_blank">Python Documentation</a>
  * <a href="https://www.jetbrains.com/help/pycharm/" rel="noopener noreferrer" target="_blank">PyCharm Documentation</a>
  * <a href="https://notepad-plus-plus.org/online-help/" rel="noopener noreferrer" target="_blank">Notepad++ Documentation</a>
  * <a href="https://www.gimp.org/tutorials/" rel="noopener noreferrer" target="_blank">GIMP Graphic Editor Documentation</a>
  * <a href="https://www.7-zip.org/" rel="noopener noreferrer" target="_blank">7-Zip Documentation</a>

### Doxygen

To achieve excellent results in documentation, it is important to precisely set up the Doxygen in a project. Otherwise, your documentation disappears in a painful valley of tears.

Once done, it can be copied as a template to other projects, which will profit from these best practice efforts too.

#### Setup Doxygen

Doxygen is configured by a single *.doxyfile file in the project main directory. To create that file, it is the best practice to copy it as a template from a similar project.

Adopt the settings by changing the project-specific options.

Be aware on the correctness of essential path settings for Doxygen:
  * INPUT
  * FILE_PATTERNS
  * EXCLUDE
  * IMAGE_PATH
  * HTML_OUTPUT

All file and folder paths must be relative to the project main directory. Do not use absolute paths. Otherwise, you will be unable to use it as a template for another project.

Review the commented settings step by step to control the Doxygen correctly.

### Create Main Page

Create the Markdown file README.md in the 'docs' folder.

Adopt the title options for the main page of your project in the *.doxyfile settings:
  * PROJECT_NAME
  * PROJECT_NUMBER
  * PROJECT_BRIEF
  * PROJECT_LOGO
  * USE_MDFILE_AS_MAINPAGE = docs/README.md

Write the project-specific content of your documentation on the main page file README.md.

See also the *.doxyfile of this project.

### Embed Code into Main Page

Any kind of text will be embedded by the "\~\~\~" statement at the beginning and the end of the text block.

To enable the code highlighting/coloring, extend the beginning of text block statement in this way:
  * \~\~\~  (No highlighting) for ASCII text, e.g. all kind of logging texts. 
  * \~\~\~{.cmd}  for batch and command line code in Windows.
  * \~\~\~{.py}  for configuration files in Linux and macOS.
  * \~\~\~{script}  for Shell Script and Bash code in Linux and macOS.
  * \~\~\~{.cpp}  for C++ code (header and body files).
  * \~\~\~{.py}  for Python code.
  * \~\~\~{.ps1}  for PowerShell code.
  * \~\~\~{.sql}  for MSSQL code.
  * etc., as the Doxygen understands the Markdown language.

Hint: To embed the content of .conf files, use "\~\~\~{.py}" statement to highlight its syntax.

### Windows Path Separator

In the common text, outside the embedded code, you must double the Windows path separator.

E.g.: 'C:\\User\\Paul\\eclipse-workspace\\pyenv-virtualenv-windows\\'. 

Otherwise, you will get dozens of warning and error messages in the Doxygen compiler output and the documentation is in parts not readable. 

### Compile Documentation

To compile the documentation with Doxygen, create a batch file like this '.\\docs\\build_doxygen_docu.bat':
  * Windows.
~~~{.cmd}
@echo off
setlocal
REM Windows Command Line Script (Batch) to build the documentation.
REM 
REM Dependencies:
REM   * Doxygen 1.13+
REM   * ..\docs.doxyfile
REM
REM © 2025 Michael Paul Korthals. All rights reserved.
REM For legal details see documentation.
REM 
REM 2025-07-10
REM
REM This script is located in the subfolder "docs"
REM in the project main directory.
REM
REM Simply open it in Windows Explorer or call it by path
REM in the Windows CMD terminal.
REM 
REM The HTML documentation will appear as subfolder ".\html".
REM
REM The script returns RC = 0 or another value in case of 
REM compilation errors.

REM Show what is going on here
echo Updating documentation ...
REM Remember the original directory
cd > ".cwd.~"
set /p ORI_DIR<".cwd.~"
del ".cwd.~"
REM Change to the drive and directory of this script
cd /d "%~dp0"
REM Change to the project root directory
REM in which the "docs" folder is located.
cd ..
REM Determine the Doxygen configuration file path
cd > ".cwd.~"
set /p CWD=<".cwd.~"
del ".cwd.~"
set "CONFIG_PATH=%CWD%\docs.doxyfile"
echo Configuring Doxygen by file:
echo %CONFIG_PATH%
REM Compile the documentation
echo Compiling. This could take a while ...
echo.
doxygen %CONFIG_PATH%
set /a RC=%ERRORLEVEL%
REM Change to the original drive and directory
cd /d %ORI_DIR%
REM Check an output return code
echo.
if %RC% neq 0 goto else1
	REM Display success
	echo [92mSUCCESS  (RC = %RC%).[0m
	echo [37mINFO     But, be aware of [93mwarnings[0m in the console log.[0m
	goto endif1
:else1
	REM Display failure
	echo [91mERROR    (RC = %RC%).[0m
	echo [95mNOTICE   Check Doxygen console logging and repair.[0m
	goto endif1
:endif1
echo.
REM Pause and exit
pause
exit /b %RC%
~~~

Executing this batch file, Doxygen produces one folder in the 'docs' folder of the project:

  * html,
  
Be aware on the log, which is produced by the Doxygen compiler. Reduce the remaining errors and warnings to zero.

### Open Documentation

To open the documentation in the default browser, create a batch file like this .\\docs\\open_doxygen_docu.bat:
 * Windows.
~~~{.cmd}
@echo off
setlocal
REM Windows Command Line Script (Batch) to build the documentation.
REM 
REM Dependencies:
REM   * Doxygen 1.13+
REM   * ..\docs.doxyfile
REM
REM © 2025 Michael Paul Korthals. All rights reserved.
REM For legal details see documentation.
REM 
REM 2025-07-10
REM
REM This script is located in the subfolder "docs"
REM in the project main directory.
REM
REM Simply open it in Windows Explorer or call it by path
REM in the Windows CMD terminal.
REM 
REM The HTML documentation will appear as subfolder ".\html".
REM
REM The script returns RC = 0 or another value in case of 
REM compilation errors.

REM Show what is going on here
echo Updating documentation ...
REM Remember the original directory
cd > ".cwd.~"
set /p ORI_DIR<".cwd.~"
del ".cwd.~"
REM Change to the drive and directory of this script
cd /d "%~dp0"
REM Change to the project root directory
REM in which the "docs" folder is located.
cd ..
REM Determine the Doxygen configuration file path
cd > ".cwd.~"
set /p CWD=<".cwd.~"
del ".cwd.~"
set "CONFIG_PATH=%CWD%\docs.doxyfile"
echo Configuring Doxygen by file:
echo %CONFIG_PATH%
REM Compile the documentation
echo Compiling. This could take a while ...
echo.
doxygen %CONFIG_PATH%
set /a RC=%ERRORLEVEL%
REM Change to the original drive and directory
cd /d %ORI_DIR%
REM Check an output return code
echo.
if %RC% neq 0 goto else1
	REM Display success
	echo [92mSUCCESS  (RC = %RC%).[0m
	echo [37mINFO     But, be aware of [93mwarnings[0m in the console log.[0m
	goto endif1
:else1
	REM Display failure
	echo [91mERROR    (RC = %RC%).[0m
	echo [95mNOTICE   Check Doxygen console logging and repair.[0m
	goto endif1
:endif1
echo.
REM Pause and exit
pause
exit /b %RC%
~~~

## Investigation

Avoid the quality reducing effect of the Internet search machines by adding quality attributes to your investigation.

Compare these examples:
  1. Search without quality attributes:
	- Google: openssl setup private certification authority
  2. Force the Google to exclude all results, which doses not contain the quality attributes in quotes:
	- Google: openssl setup private certification authority 'Key Usage' 'Subject Alternative Name' 

As you see, 
  * the 1st investigation is overcrowded by instructions, which are incomplete or cannot be trusted,
  * the 2nd investigation moves the wanted results near to pole position and nearly does not show any trash on the first results page.

This tactic increases the efficiency of the whole software development.

## Data Backup

A manual Backup job must be configured in your Site Service Application. From there it can be explicitly executed. 

Security: It is recommended to do this once every working day in minimum. In addition, after finishing every development milestone. 

## Security Risk Analysis

In professional software development, we have to follow a few rules for the most part. Otherwise, the remaining risks must be consciously accepted.

Out of the "IT-Grundschutz-Compendium" from Federal Office for Information Security (BSI) in Germany (<a href="https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Grundschutz/International/bsi_it_gs_comp_2022.pdf?__blob=publicationFile&v=2" rel="noopener noreferrer" target="_blank">Download</a>) has been selected as applicable for designing this Software Utility:
  * CON.8.A5 Secure System Design (B)
  * CON.8.A6 Use of External Libraries from Trusted Sources (B)

This risk analysis has been performed by the author on 2025-07-11 07:00:00.

Result of risk analysis:
  * Zero deviations.
    * See details/results/comments in the following 2 subunits.

### CON.8.A5 Secure System Design (B)

The following basic rules of secure system design MUST be considered in the software to be developed:
  * All input data MUST be checked and validated before further processing takes place.
    * FULFILLED: See sources of PyPI installer and Windows/Linux Command Line utility scripts in detail. 
  * For client-server applications, the data MUST be validated on the server side.
    * NOT APPLICABLE. 
  * The software's default settings MUST be set to facilitate secure operation.
    * NOT APPLICABLE. 
  * In the event of errors in or failures of system components, sensitive information MUST NOT be disclosed.
    * FULFILLED. Only directory names, file names and some technical facts are logged by this application and surrounding components. The logging is sent to console only. 
  * It MUST be possible to run the software with as few privileges as possible.
    * FULFILLED: These script are running under normal OS user privileges. But, it is also possible to use OS admin privileges it the application requires this.
  * Sensitive data MUST be transmitted and stored in encrypted form according to the specifications of the crypto concept at hand.
    * NOT APPLICABLE.
  * Trusted mechanisms that meet the security requirements of the application in question MUST be used for user authentication and access.
    * FULFILLED: See the 'PyPI' security measures (code-signing, HTTPS file transfer).
  * If passwords are stored for authentication, they MUST be stored using a secure hash procedure.
    * NOT APPLICABLE.
  * Security-relevant events MUST be logged in such a way that they can be evaluated afterward.
    * NOT APPLICABLE.
  * Information that is not relevant for productive operation (e.g. comments with access data for the development environment) SHOULD be removed in delivered program code and configuration files.
    * FULFILLED: The productive code does not contain any temporary developer notes or unnecessary code commented code sequences.
  *  The system design MUST be documented. It MUST be verified that the system design meets all the relevant security requirements.
    * FULFILLED: See this comprehensive documentation and comments in the code.

### CON.8.A6 Use of External Libraries from Trusted Sources (B)

  * If external libraries are used as part of the development and implementation process, they MUST be obtained from trusted sources. Before external libraries are used, their integrity MUST be ensured.
    * FULFILLED. Cygwin, Python, PyCharm Community Edition, Notepad++ Source Editor, GIMP Graphic Editor and are OpenSource and reviewed by big communities. The related contributors are trusted worldwide.

## Publication on GitHub

To share the sources of the 'pyenv-virtualenv' for Windows plugin, GitHub is the application of choice.

There, the plugin is published as Open Source repository.

This repository holds the pictures and its supporting document 'README.md'.

In addition, the Doxygen Industry Standard Documentation is provided as ZIP file in that repository.

> IMPORTANT NOTE: The project/repository name 'pyenv-virtualenv-windows' on PyPI and GitHub must be identical.

### Authentication

This publication requires strong Security measures to protect the source. So, Two-Factor Authentication (2FA) must be activated on GitHub. 

The TOTP generator (e.g. Google Authenticator) must be installed on your smartphone or tablet and capable to continuously deliver the time-based OTP for GitHub. The GitHub password and the list of 2FA recovery codes must be securely stored in your password safe.

### Code of Conduct

This project included collaboration with people in these cases:
* Getting 'issues' to clarify problems and situations.
* Getting 'pull requests', which lead to improvements.

Any collaboration with people must be regulated/enforced by defined rules of engagement.

In this project we use version 2.1 of the Contributor Covenant, published with the courtesy of the organization of the same name 
<a href="https://www.contributor-covenant.org/" rel="noopener noreferrer" target="_blank">https://www.contributor-covenant.org/</a>.  

See the file 'CODE_OF_CONDUCT.md' in the project main folder, locally and on GitHub.

Also, see the related chapter in the file 'README.md' on GitHub. 

### Upload

> NOTE: GitHub does not accept empty folders. In addition, it is not possible to create an empty folder like in Windows Explorer.

> NOTE: GitHub rejects bulk uploads of more than 100 files. It's also not a good idea to upload the Doxygen documentation with its hundreds of files, as it's not provided by GitHub anyway.
 
So, to prepare the upload, temporarily remove the 'docs\\html' folder.

Use the "Upload files" feature to uploads files and folders to the GitHub repository 'pyenv-virtualenv-windows'.

Finally, restore the 'docs\\html' by compiling the documentation:
~~~{.cmd}
"%USERPROFILE%\eclipse-workspace\pyenv-virtualenv-windows\src\pyenv-virtualenv-windows\docs\build_doxygen_docs.bat"
~~~

## Publication on PyPI

It is my declared goal to share this product to the world. I have seen the gap in 'pyenv' and from the beginning it is my intention to close it.

Now, the working product of this project, the plugin 'pyenv-virtualenv' for Windows will be published worldwide on the relevant repositories:
* Test PyPI: to test the new package.
* PyPI : to release the new package to the wordwide Python community.

> IMPORTANT NOTE: The project name 'pyenv-virtualenv-windows' on Test PyPI, PyPI and GitHub repositories must be identical.

> NOTE: We are using the different PYPI_README.md on PyPI and README.md on GitHub. Reason: PiPI does not allow to store or redirect images. 

Therefore, the images, which are essential for the didactic supplementation of the supporting documents README.md, are stored exclusively on GitHub or in the downloadable Doxygen Industry Standard Documentation.

> NOTE: PyPI refuses to integrate the project's Doxygen Industry Standard Documentation, which is enhanced with images and provided in HTML format. 
 
The Doxygen Industry Standard Documentation must be published separately in a ZIP file on GitHub.

### Authentication

This publication requires strong Security measures to protect the published package and its testing counterpart. So, Two-Factor Authentication (2FA) must be activated in the user profiles on PiPI and Test PyPI. 

The TOTP generator (e.g. Google Authenticator) must be installed on your smartphone or tablet and capable to continuously deliver the time-based OTPs for PyPI and Test PyPI. For both repositories, the password and the list of 2FA reset codes must be securely stored in separate entries in your password safe.

### Preparation

To simplify the publication, I abstracted this preparation from packaging. 

#### Global Python Version

First of all, the installed global Python version in pyenv must be prepared to publish the product.

> NOTE: Be sure that the prompt in the Windows console terminal is cleared from Python virtual environments. Otherwise, deactivate it.

Then let's start with these commands:
~~~{.cmd}
REM 1. Check which Python version is global
pyenv versions
REM 2. Check if the 'pyenv' global Python version is correctly set.
python -c "import sys; print(sys.executable); quit()"
REM 3. Check the package list.
pip list
~~~
Expected Output (e.g.):
~~~
C:\Users\Paul\eclipse-workspace\cinema_5>pyenv versions
* 3.12.10 (set by C:\Users\Paul\eclipse-workspace\cinema_5\.python-version)
  3.13.5
  3.3.5
  3.6.8
  3.9.13
  cinema_5-3.12.10
  site_3-3.12.10

C:\Users\Paul\eclipse-workspace\cinema_5>python -c "import sys; print(sys.executable); quit()"
C:\Users\Paul\.pyenv\pyenv-win\versions\3.12.10\python.exe

C:\Users\Paul\eclipse-workspace\cinema_5>pip list
Package      Version
------------ -------
distlib      0.3.9
filelock     3.18.0
pip          25.0.1
platformdirs 4.3.8
virtualenv   20.31.2
~~~

Only a few packages (pip, virtualenv) and its subpackages are installed within the global Python version. This is the correct state before the first publication. 

#### Required Packages

According to the PyPI documentation, ensure by these command that pip, setuptools, wheel, build, twine are installed and up-to-date:
~~~{.cmd}
REM  1. Install/upgrade publication relevant utility packages  
python -m pip install --upgrade pip setuptools wheel build twine
REM 2. Check/freeze the package list.
pip list
pip freeze > "{project main directory}\requirements.txt"
~~~
Output (e.g.):
~~~
C:\Users\Paul\eclipse-workspace\cinema_5>python -m pip install --upgrade pip setuptools wheel build twine readme-coverage-badger
Requirement already satisfied: pip in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (25.0.1)
Collecting pip
  Using cached pip-25.1.1-py3-none-any.whl.metadata (3.6 kB)
Collecting setuptools
  Using cached setuptools-80.9.0-py3-none-any.whl.metadata (6.6 kB)
Collecting wheel
  Using cached wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)
Using cached pip-25.1.1-py3-none-any.whl (1.8 MB)
Using cached setuptools-80.9.0-py3-none-any.whl (1.2 MB)
Using cached wheel-0.45.1-py3-none-any.whl (72 kB)
Installing collected packages: wheel, setuptools, pip
  Attempting uninstall: pip
    Found existing installation: pip 25.0.1
    Uninstalling pip-25.0.1:
      Successfully uninstalled pip-25.0.1
Successfully installed pip-25.1.1 setuptools-80.9.0 wheel-0.45.1
Collecting build
  Downloading build-1.2.2.post1-py3-none-any.whl.metadata (6.5 kB)
Collecting packaging>=19.1 (from build)
  Downloading packaging-25.0-py3-none-any.whl.metadata (3.3 kB)
Collecting pyproject_hooks (from build)
  Downloading pyproject_hooks-1.2.0-py3-none-any.whl.metadata (1.3 kB)
Collecting colorama (from build)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Downloading build-1.2.2.post1-py3-none-any.whl (22 kB)
Downloading packaging-25.0-py3-none-any.whl (66 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Downloading pyproject_hooks-1.2.0-py3-none-any.whl (10 kB)
Installing collected packages: pyproject_hooks, packaging, colorama, build
Successfully installed build-1.2.2.post1 colorama-0.4.6 packaging-25.0 pyproject_hooks-1.2.0
Collecting twine
  Downloading twine-6.1.0-py3-none-any.whl.metadata (3.7 kB)
Collecting readme-renderer>=35.0 (from twine)
  Using cached readme_renderer-44.0-py3-none-any.whl.metadata (2.8 kB)
Collecting requests>=2.20 (from twine)
  Downloading requests-2.32.4-py3-none-any.whl.metadata (4.9 kB)
Collecting requests-toolbelt!=0.9.0,>=0.8.0 (from twine)
  Using cached requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
Collecting urllib3>=1.26.0 (from twine)
  Downloading urllib3-2.5.0-py3-none-any.whl.metadata (6.5 kB)
Collecting keyring>=15.1 (from twine)
  Downloading keyring-25.6.0-py3-none-any.whl.metadata (20 kB)
Collecting rfc3986>=1.4.0 (from twine)
  Using cached rfc3986-2.0.0-py2.py3-none-any.whl.metadata (6.6 kB)
Collecting rich>=12.0.0 (from twine)
  Using cached rich-14.0.0-py3-none-any.whl.metadata (18 kB)
Requirement already satisfied: packaging>=24.0 in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from twine) (25.0)
Collecting id (from twine)
  Using cached id-1.5.0-py3-none-any.whl.metadata (5.2 kB)
Collecting pywin32-ctypes>=0.2.0 (from keyring>=15.1->twine)
  Downloading pywin32_ctypes-0.2.3-py3-none-any.whl.metadata (3.9 kB)
Collecting jaraco.classes (from keyring>=15.1->twine)
  Downloading jaraco.classes-3.4.0-py3-none-any.whl.metadata (2.6 kB)
Collecting jaraco.functools (from keyring>=15.1->twine)
  Downloading jaraco_functools-4.2.1-py3-none-any.whl.metadata (2.9 kB)
Collecting jaraco.context (from keyring>=15.1->twine)
  Using cached jaraco.context-6.0.1-py3-none-any.whl.metadata (4.1 kB)
Collecting nh3>=0.2.14 (from readme-renderer>=35.0->twine)
  Downloading nh3-0.3.0-cp38-abi3-win_amd64.whl.metadata (2.1 kB)
Collecting docutils>=0.21.2 (from readme-renderer>=35.0->twine)
  Using cached docutils-0.21.2-py3-none-any.whl.metadata (2.8 kB)
Collecting Pygments>=2.5.1 (from readme-renderer>=35.0->twine)
  Downloading pygments-2.19.2-py3-none-any.whl.metadata (2.5 kB)
Collecting charset_normalizer<4,>=2 (from requests>=2.20->twine)
  Downloading charset_normalizer-3.4.2-cp312-cp312-win_amd64.whl.metadata (36 kB)
Collecting idna<4,>=2.5 (from requests>=2.20->twine)
  Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
Collecting certifi>=2017.4.17 (from requests>=2.20->twine)
  Downloading certifi-2025.7.14-py3-none-any.whl.metadata (2.4 kB)
Collecting markdown-it-py>=2.2.0 (from rich>=12.0.0->twine)
  Using cached markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=12.0.0->twine)
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Collecting more-itertools (from jaraco.classes->keyring>=15.1->twine)
  Downloading more_itertools-10.7.0-py3-none-any.whl.metadata (37 kB)
Downloading twine-6.1.0-py3-none-any.whl (40 kB)
Downloading keyring-25.6.0-py3-none-any.whl (39 kB)
Downloading pywin32_ctypes-0.2.3-py3-none-any.whl (30 kB)
Using cached readme_renderer-44.0-py3-none-any.whl (13 kB)
Using cached docutils-0.21.2-py3-none-any.whl (587 kB)
Downloading nh3-0.3.0-cp38-abi3-win_amd64.whl (604 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 604.5/604.5 kB 7.4 MB/s eta 0:00:00
Downloading pygments-2.19.2-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 12.3 MB/s eta 0:00:00
Downloading requests-2.32.4-py3-none-any.whl (64 kB)
Downloading charset_normalizer-3.4.2-cp312-cp312-win_amd64.whl (105 kB)
Using cached idna-3.10-py3-none-any.whl (70 kB)
Downloading urllib3-2.5.0-py3-none-any.whl (129 kB)
Downloading certifi-2025.7.14-py3-none-any.whl (162 kB)
Using cached requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
Using cached rfc3986-2.0.0-py2.py3-none-any.whl (31 kB)
Using cached rich-14.0.0-py3-none-any.whl (243 kB)
Using cached markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Using cached id-1.5.0-py3-none-any.whl (13 kB)
Downloading jaraco.classes-3.4.0-py3-none-any.whl (6.8 kB)
Using cached jaraco.context-6.0.1-py3-none-any.whl (6.8 kB)
Downloading jaraco_functools-4.2.1-py3-none-any.whl (10 kB)
Downloading more_itertools-10.7.0-py3-none-any.whl (65 kB)
Installing collected packages: urllib3, rfc3986, pywin32-ctypes, Pygments, nh3, more-itertools, mdurl, jaraco.context, idna, docutils, charset_normalizer, certifi, requests, readme-renderer, markdown-it-py, jaraco.functools, jaraco.classes, rich, requests-toolbelt, keyring, id, twine
Successfully installed Pygments-2.19.2 certifi-2025.7.14 charset_normalizer-3.4.2 docutils-0.21.2 id-1.5.0 idna-3.10 jaraco.classes-3.4.0 jaraco.context-6.0.1 jaraco.functools-4.2.1 keyring-25.6.0 markdown-it-py-3.0.0 mdurl-0.1.2 more-itertools-10.7.0 nh3-0.3.0 pywin32-ctypes-0.2.3 readme-renderer-44.0 requests-2.32.4 requests-toolbelt-1.0.0 rfc3986-2.0.0 rich-14.0.0 twine-6.1.0 urllib3-2.5.0
Collecting readme-coverage-badger
  Downloading readme_coverage_badger-1.0.1-py3-none-any.whl.metadata (29 kB)
Requirement already satisfied: colorama in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from readme-coverage-badger) (0.4.6)
Collecting coverage (from readme-coverage-badger)
  Downloading coverage-7.9.2-cp312-cp312-win_amd64.whl.metadata (9.1 kB)
Downloading readme_coverage_badger-1.0.1-py3-none-any.whl (16 kB)
Downloading coverage-7.9.2-cp312-cp312-win_amd64.whl (215 kB)
Installing collected packages: coverage, readme-coverage-badger
Successfully installed coverage-7.9.2 readme-coverage-badger-1.0.1

C:\Users\Paul\eclipse-workspace\cinema_5>pip list
build                  1.2.2.post1
certifi                2025.7.14
charset-normalizer     3.4.2
colorama               0.4.6
coverage               7.9.2
distlib                0.3.9
docutils               0.21.2
filelock               3.18.0
id                     1.5.0
idna                   3.10
jaraco.classes         3.4.0
jaraco.context         6.0.1
jaraco.functools       4.2.1
keyring                25.6.0
markdown-it-py         3.0.0
mdurl                  0.1.2
more-itertools         10.7.0
nh3                    0.3.0
packaging              25.0
pip                    25.1.1
platformdirs           4.3.8
Pygments               2.19.2
pyproject_hooks        1.2.0
pywin32-ctypes         0.2.3
readme-coverage-badger 1.0.1
readme_renderer        44.0
requests               2.32.4
requests-toolbelt      1.0.0
rfc3986                2.0.0
rich                   14.0.0
setuptools             80.9.0
twine                  6.1.0
urllib3                2.5.0
virtualenv             20.31.2
wheel                  0.45.1
~~~

#### API Token

The repositories Test PyPI and PyPI are using strong measures to secure uploading packages.

On each repository go to your user profile and generate the API token.

Store these token strings immediately into the protected memo fields in your password safe, separately for Test PyPI and PyPi.

Afterward, create the repository configuration file in your user profile on your development workstation:
~~~
REM On Windows:
%USERPROFILE%\.pypirc
# On Posix/Linux:
~/.pypirc
~~~
Content Template:
~~~
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-{Insert the cryptic API token code string for PyPI}

[testpypi]
username = __token__
password = pypi-{Insert the cryptic API token code string for Test PyPI}
~~~

User name is the word '__token__'.
Password is the complete API token of that repository, starting with 'pypy-'. Not starting with 'pypi-pypi-'.

> SECURITY: Passwords and other confidential data must not be stored in scripts and configuration files. 
 
Instead of using the 'password' field, you must save your API tokens and passwords securely using 'keyring' (which is installed by 'twine').

Commands to set the API tokens into 'keyring': 
~~~
keyring set https://test.pypi.org/legacy/ __token__
keyring set https://upload.pypi.org/legacy/ __token__
~~~

Commands to check if the API tokens exist on 'keyring': 
~~~
keyring get https://test.pypi.org/legacy/ __token__
keyring get https://upload.pypi.org/legacy/ __token__
~~~

After the 'keyring' password storage is working perfectly, the content of the '.pypirc' file in the user profile directory can be reduced to this non-compromising variant:
~~~
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__

[testpypi]
username = __token__
~~~

#### Setup Local Test System

To successfully test the whole publication at the end, a Windows test system is needed.

> NOTE: 'Fresh' in this context means that it completely fulfills the actual Microsoft system requirements for that platform. In addition, Python, 'pyenv' 'virtualenv', 'pyenv-virtualenv' and other software have never been installed inside that image.

E.g.:
* Fresh installed Windows 11 Intel x64 Laptop/Workstation.
* Fresh installed Windows Intel x64 Server.

For more efficiency clone and activate Windows platform images e.g. on an Ubuntu Linux Kernel-based Virtual Machine (KVM): 
* Fresh Virtual Windows 11 Intel x64 client image.
* Fresh Virtual Windows Intel x64 server image.  

### Packaging

To set up the package, or to update it for a new version, these information will help: 
*  <a href="https://packaging.python.org/en/latest/" rel="noopener noreferrer" target="_blank">Python Packaging User Guide</a>
  * Official instruction set by the Python Packaging Authority. Explore it deep to get complete information. 
*  <a href="https://packaging.python.org/en/latest/tutorials/packaging-projects/" rel="noopener noreferrer" target="_blank">Packaging Python Projects</a>
  * This tutorial walks you through how to package a simple Python project. It will show you how to add the necessary files and structure to create the package, how to build the package, and how to upload it to the Python Package Index (PyPI).

#### Configure

Display the folder tree of the project and the project root folder files:
Commands:
~~~
tree .
dir
~~~
Output:
~~~
C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>tree .
%USERPROFILE%\eclipse-workspace\pyenv-virtualenv-windows
├───.idea
│   └───inspectionProfiles
├───dist
├───src
│   ├───pyenv-virtualenv-windows
│   │   ├───.experiments
│   │   │   ├───bin
│   │   │   ├───shims
│   │   │   └───versions
│   │   ├───.idea
│   │   │   ├───dictionaries
│   │   │   └───inspectionProfiles
│   │   ├───bin
│   │   │   └───lib
│   │   │       └───__pycache__
│   │   ├───docs
│   │   │   └───images
│   │   ├───libexec
│   │   ├───patch
│   │   └───shims
│   └───pyenv_virtualenv_windows.egg-info
└───tests

C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>dir
 Datenträger in Laufwerk C: ist SYSTEM
 Volumeseriennummer: 38E4-3A30

 Verzeichnis von C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows

Sa, 26. 07. 2025  12:31    <DIR>          .
Do, 17. 07. 2025  02:12    <DIR>          ..
Sa, 19. 07. 2025  07:14             5.217 .gitignore
Do, 17. 07. 2025  05:11    <DIR>          .idea
Mo, 28. 07. 2025  01:25    <SYMLINK>      CHANGELOG.md [src\pyenv-virtualenv-windows\CHANGELOG.md]
Mo, 21. 07. 2025  02:54             5.473 CODE_OF_CONDUCT.md
Sa, 26. 07. 2025  12:31    <DIR>          dist
Do, 17. 07. 2025  04:55    <SYMLINK>      LICENSE [src\pyenv-virtualenv-windows\LICENSE.txt]
Sa, 26. 07. 2025  12:29                19 MANIFEST.in
Sa, 26. 07. 2025  12:03             2.706 PYPI_README.md
Sa, 26. 07. 2025  10:01             1.023 pyproject.toml
Sa, 26. 07. 2025  12:18            50.477 README.md
Di, 22. 07. 2025  04:23                17 requirements.txt
Mo, 21. 07. 2025  09:28               623 requirements_author.txt
Di, 22. 07. 2025  04:23                17 requirements_user.txt
Do, 17. 07. 2025  09:04    <DIR>          src
Do, 17. 07. 2025  02:36    <DIR>          tests
              10 Datei(en),         65.572 Bytes
               6 Verzeichnis(se), 71.254.540.288 Bytes frei
~~~

Structure the folder tree according to the instructions in the tutorials. 

Important are these files and folders:
  * src\
    * Parent folder of the plugin root folder.
  * dist\
    * Distribution folder, where the resulting packages can be found.
  * tests\
    * Folder for scrips to automate testing the package (empty, not used).  
  * README.md
    * Short instruction to install and use the plugin. Published on GitHub only.
  * PYPI_README.md
    * Tiny fragment of information on PyPI, just to direct the user to read README.md on GitHub or to download and study the Doxygen Industry Standard documentation.
  * CHANGELOG.md
    * List of versions in descending order, describing the changes done for each version. 
  * LICENSE
    * Symlink to the license document in the plugin root folder.
  * MANIFEST.in
    * File to configure, e.g., to exclude files from the package or to include files and folders into the Python package. 
  * pyproject.toml
    * PyPI package configuration file.
  * .gitignore
    * Downloaded copy of the filter configuration to prevent obsolete files and folders uploading to the GitHub repository. E.g. the Doxygen 'html' folder, which contains hundreds of files, which are uneasily to manage by the GitHub cloud application methods. 

Create/update the file 'pyproject.toml':
~~~{.toml}
[build-system]
requires = ["setuptools >= 77.0.3"]
build-backend = "setuptools.build_meta"

[project]
name = "pyenv-virtualenv-windows"
version = "1.2.4"
authors = [
  { name="Michael Paul Korthals", email="michael_paul.korthals@chello.at" },
]
description = "A 'pyenv' plugin to manage Python virtual environments, depending on different Python versions, for various Python projects."
readme = "PYPI_README.md"
requires-python = ">=3.6"
dependencies = [
  "virtualenv"
]
classifiers = [
	"Development Status :: 4 - Beta",
	"Environment :: Console",
	"Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Operating System :: Microsoft :: Windows",
]
license = "GPL-3.0-only"
license-files = ["LICENSE*"]

[project.urls]
Homepage = "https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/"
Issues = "https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/issues"
~~~

See description for each of these settings and more the PyPI documentation.

In addition, we must exclude the GitHub 'README.md' from the package. Otherwise, information with image dead links will appear in the PyPI package description text. This behaviour will be enforced by this file in the project root folder:
~~~{.cmd}
notepad++ MANIFEST.in 
type MANIFEST.in
~~~
Output:
~~~
exclude README.md
exclude CHANGELOG.md
include src/pyenv-virtualenv-windows/.tree-excludes
include src/pyenv-virtualenv-windows/.version
include src/pyenv-virtualenv-windows/CHANGELOG.md
include src/pyenv-virtualenv-windows/docs.doxyfile
include src/pyenv-virtualenv-windows/INDEX.md
include src/pyenv-virtualenv-windows/install*.*
include src/pyenv-virtualenv-windows/LICENSE.txt
include src/pyenv-virtualenv-windows/README.bat
recursive-include src/pyenv-virtualenv-windows/docs/ * *.*
recursive-exclude src/pyenv-virtualenv-windows/docs/.idea * *.*
exclude src/pyenv-virtualenv-windows/docs/*.zip
exclude src/pyenv-virtualenv-windows/docs/*.backup
recursive-include src/pyenv-virtualenv-windows/bin/ * *.*
exclude src/pyenv-virtualenv-windows/bin/lib/__pycache__/*.pyc
exclude src/pyenv-virtualenv-windows/bin/lib/__pycache__/
precursive-include src/pyenv-virtualenv-windows/libexec/ * *.*
recursive-include src/pyenv-virtualenv-windows/patch/ * *.*
recursive-include src/pyenv-virtualenv-windows/shims/ * *.*
~~~

The line 'exclude README.md' prevents 'twine' from including the GitHub project documentation 'README.md' with the broken image links in the PyPI packages.

The other lines include missing files and folders into the package and also exclude further obsolete files and folders.

NOTE: Don't forget to build the documentation using the related batch script in the plugin root 'docs' folder.

If everything is crystal-clear fine configured, then step forward to the next unit. 

#### Build Package

Use this command to build/compile the package:
~~~{.cmd}
python -m build
echo %errorlevel%
~~~
Output:
~~~
C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>python -m build
* Creating isolated environment: venv+pip...
* Installing packages in isolated environment:
  - setuptools >= 77.0.3
* Getting build dependencies for sdist...
...
...
Successfully built pyenv_virtualenv_windows-1.2.4.tar.gz and pyenv_virtualenv_windows-1.2.4-py3-none-any.whl

C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>echo %errorlevel%
0
~~~

If the call returns 0 and not any error or warning is visible in the console log, then step forward to the next unit.

### Check Package

Familiarize yourself with the 'twine' application, which allows you to try out the complex upload to Test PyPI at your leisure.

Afterward check the file path to the package of that specific version using 'twine':
~~~{.cmd}
python -m twine check dist/pyenv_virtualenv_windows-1.2.4*.*
~~~
Output:
~~~
C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>python -m twine check dist/pyenv_virtualenv_windows-1.2.4*.*
Checking dist\pyenv_virtualenv_windows-1.2.4-py3-none-any.whl: PASSED
Checking dist\pyenv_virtualenv_windows-1.2.4.tar.gz: PASSED
~~~

In addition, check if the all the files are included into the specific version of the package:
~~~{.cmd}
tar -tf dist/pyenv_virtualenv_windows-1.2.4*.tar.gz
~~~
Output with missing '.tree_excludes', '.version', 'install*.*' 'docs\\' (recursively) , e.g.:
~~~
C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>tar -tf dist/pyenv_virtualenv_windows-1.2.4*.tar.gz
pyenv_virtualenv_windows-1.2.4/
pyenv_virtualenv_windows-1.2.4/LICENSE
pyenv_virtualenv_windows-1.2.4/MANIFEST.in
pyenv_virtualenv_windows-1.2.4/PKG-INFO
pyenv_virtualenv_windows-1.2.4/PYPI_README.md
pyenv_virtualenv_windows-1.2.4/pyproject.toml
pyenv_virtualenv_windows-1.2.4/setup.cfg
pyenv_virtualenv_windows-1.2.4/src/
pyenv_virtualenv_windows-1.2.4/src/pyenv-virtualenv-windows/
pyenv_virtualenv_windows-1.2.4/src/pyenv-virtualenv-windows/bin/
pyenv_virtualenv_windows-1.2.4/src/pyenv-virtualenv-windows/bin/lib/
pyenv_virtualenv_windows-1.2.4/src/pyenv-virtualenv-windows/bin/lib/hlp.py
pyenv_virtualenv_windows-1.2.4/src/pyenv-virtualenv-windows/bin/lib/log.py
pyenv_virtualenv_windows-1.2.4/src/pyenv-virtualenv-windows/bin/lib/tbl.py
pyenv_virtualenv_windows-1.2.4/src/pyenv-virtualenv-windows/bin/lib/tre.py
pyenv_virtualenv_windows-1.2.4/src/pyenv-virtualenv-windows/bin/pyenv-virtualenv-delete.py
pyenv_virtualenv_windows-1.2.4/src/pyenv-virtualenv-windows/bin/pyenv-virtualenv-prefix.py
pyenv_virtualenv_windows-1.2.4/src/pyenv-virtualenv-windows/bin/pyenv-virtualenv-props.py
pyenv_virtualenv_windows-1.2.4/src/pyenv-virtualenv-windows/bin/pyenv-virtualenv.py
pyenv_virtualenv_windows-1.2.4/src/pyenv-virtualenv-windows/bin/pyenv-virtualenvs.py
pyenv_virtualenv_windows-1.2.4/src/pyenv_virtualenv_windows.egg-info/
pyenv_virtualenv_windows-1.2.4/src/pyenv_virtualenv_windows.egg-info/PKG-INFO
pyenv_virtualenv_windows-1.2.4/src/pyenv_virtualenv_windows.egg-info/SOURCES.txt
pyenv_virtualenv_windows-1.2.4/src/pyenv_virtualenv_windows.egg-info/dependency_links.txt
pyenv_virtualenv_windows-1.2.4/src/pyenv_virtualenv_windows.egg-info/requires.txt
pyenv_virtualenv_windows-1.2.4/src/pyenv_virtualenv_windows.egg-info/top_level.txt
~~~

In case of missing files, these must be explicitly included into the 'MANIFEST.in' file. Content:
~~~
exclude README.md
exclude CHANGELOG.md
include src/pyenv-virtualenv-windows/.tree-excludes
include src/pyenv-virtualenv-windows/.version
include src/pyenv-virtualenv-windows/CHANGELOG.md
include src/pyenv-virtualenv-windows/docs.doxyfile
include src/pyenv-virtualenv-windows/INDEX.md
include src/pyenv-virtualenv-windows/install*.*
include src/pyenv-virtualenv-windows/LICENSE.txt
include src/pyenv-virtualenv-windows/README.bat
recursive-include src/pyenv-virtualenv-windows/docs/ * *.*
recursive-exclude src/pyenv-virtualenv-windows/docs/.idea * *.*
exclude src/pyenv-virtualenv-windows/docs/*.zip
exclude src/pyenv-virtualenv-windows/docs/*.backup
recursive-include src/pyenv-virtualenv-windows/bin/ * *.*
exclude src/pyenv-virtualenv-windows/bin/lib/__pycache__/*.pyc
exclude src/pyenv-virtualenv-windows/bin/lib/__pycache__/
precursive-include src/pyenv-virtualenv-windows/libexec/ * *.*
recursive-include src/pyenv-virtualenv-windows/patch/ * *.*
recursive-include src/pyenv-virtualenv-windows/shims/ * *.*
~~~

If everything is crystal-clear and not any deviation is visible in the console log, then step forward to the next unit. Otherwise, step back, correct and try again.

### Upload to Test PyPI

> IMPORTANT RESTRICTION: A package of a specific version can only be uploaded once. If something is failing afterward, a new version with a new bugfix number inside the version number must be created. 
 
> WARNING: Don't use undocumented PyPI easter-eggs from inofficial sources, which try to bypass this restriction.   

To avoid unnecessary and obsolete communication efforts in a test phase of your project, use the 'Test PyPI' repository for first to upload the new package. The essential requirements for this step see in Unit 'Preparations'.

Use this command to upload the new version package to PyPI:
~~~{.cmd}
python -m twine upload --repository testpypi dist/pyenv_virtualenv_windows-1.2.4*.*
echo %errorlevel%
~~~
Output e.g.:
~~~
C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>python -m twine upload --repository testpypi dist/pyenv_virtualenv_windows-1.2.4*.*
Uploading distributions to https://test.pypi.org/legacy/
Uploading pyenv_virtualenv_windows-1.2.4-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 112.1/112.1 kB • 00:00 • 6.0 MB/s
Uploading pyenv_virtualenv_windows-1.2.4.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 124.5/124.5 kB • 00:00 • ?

View at:
https://test.pypi.org/project/pyenv-virtualenv-windows/1.2.4/

C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>echo %errorlevel%
0
~~~

If the call returns 0 and not any error or warning is visible in the console log, then step forward to the next unit.

### Final Test

Use the prepared Windows Test System to install, configure and perform a full test according to the User Manual of 'pyenv-virtualenv' for Windows:
1. 'pyenv' for Windows
2. 'pyenv-virtualenv' for Windows

When testing, don't forget to observe the behavior of 'install.bat' and its sub processes in case of PATH conflicts. Simulate the related situations by setting incorrect 'User' PATH and critical 'Machine' PATH. See unit 'Path Conflicts' in the user manual. 

If everything is fine and the final test performed successfully, you are allowed to step forward to the next unit.

### Upload to PyPI

> IMPORTANT RESTRICTION: A package of a specific version can only be uploaded once. If something is failing afterward, a new version with a new bugfix number inside the version number must be created. 
 
> WARNING: Don't use undocumented PyPI easter-eggs from inofficial sources, which try to bypass this restriction.   

Use this command to upload the new version package to PyPI:
~~~{.cmd}
python -m twine upload --repository pypi dist/pyenv_virtualenv_windows-1.2.4*.*
echo %errorlevel%
~~~
Output e.g.:
~~~
C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>python -m twine upload --repository pypi dist/pyenv_virtualenv_windows-1.2.4*.*
Uploading distributions to https://upload.pypi.org/legacy/
Uploading pyenv_virtualenv_windows-1.2.4-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 112.1/112.1 kB • 00:00 • 678.6 kB/s
Uploading pyenv_virtualenv_windows-1.2.4.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 124.5/124.5 kB • 00:00 • 864.7 kB/s

View at:
https://pypi.org/project/pyenv-virtualenv-windows/1.2.4/

C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>echo %errorlevel%
0
~~~

If everything is fine, the publication is successfully placed on PyPI. Everybody can access it. Worldwide. 

# Development Manual

In this chapter you get detailed information how to develop in this project.

Knowledge about software development administration of Posix/Linux and Windows operating systems, PyPI Package installers, Windows and Linux command line interface, Python, Powershell and CMD scripting languages are required to understand this documentation.

## Reverse Engineering

This Plugin in working in Linux, macOS and possibly other Posix platforms. It is written in BASH scripting language.

Code translation is too difficult. 

It is easier to reverse engineer the plugin with the same behaviour for Windows.

### Plugin Interface

The Windows version of 'pyenv' locates all plugin launchers in this folder:
~~~
%PYENV_ROOT%libexec
~~~

So, it is easy to install the new plug-in 'pyenv-virtualenv' by creating these working batch files in that folder:
~~~
%PYENV_ROOT%libexec\pyenv-virtualenv.bat
%PYENV_ROOT%libexec\pyenv-activate.bat
%PYENV_ROOT%libexec\pyenv-deactivate.bat
~~~
These batch files are link-like launchers only, which are relatively calling the substantial batch files and forwarding arguments.

1. Code of the 'pyenv virtualenv {version} {name}' launcher:
~~~{.CMD}
@echo off
call %~dp0..\plugins\pyenv-virtualenv\bin\pyenv-virtualenv.bat %*
~~~
Inspect related batch code in 'pyenv-virtualenv.bat'.

2. Code of the 'pyenv activate [{name}]' launcher:
~~~{.CMD}
@echo off
call %~dp0..\shims\activate.bat %*
~~~
Inspect related batch code in 'activate.bat':

3. Code of the 'pyenv deactivate' launcher:
~~~{.CMD}
@echo off
call deactivate.bat
~~~
The related 'deactivate' batch code is automatically generated by the 'pyenv virtualenv {version} {name}' command, when python generates the virtual environment.

Each 'pyenv virtualenv' command call including further arguments is calling the subroutines of this plugin, which are located in:
~~~
%PYENV_ROOT%plugins\pyenv-virtualenv\bin
~~~

Plugin subroutines:
~~~{.cmd}
C:\Users\Paul\.pyenv\pyenv-win\plugins\pyenv-virtualenv\bin>ls -l
total 58
-rwx------+ 1 Paul Kein   788 Jun 22 20:05 pyenv-activate
-rwx------+ 1 Paul Kein   440 Jun 22 20:05 pyenv-deactivate
-rwx------+ 1 Paul Kein  7307 Jun 22 20:05 pyenv-sh-activate
-rwx------+ 1 Paul Kein  4149 Jun 22 20:05 pyenv-sh-deactivate
-rwx------+ 1 Paul Kein 19282 Jun 22 20:05 pyenv-virtualenv
-rwx------+ 1 Paul Kein  2385 Jun 22 20:05 pyenv-virtualenv-delete
-rwx------+ 1 Paul Kein  3149 Jun 22 20:05 pyenv-virtualenv-prefix
-rwx------+ 1 Paul Kein    92 Jun 29 00:46 pyenv-virtualenv.bat
-rwx------+ 1 Paul Kein     0 Jun 29 00:38 pyenv-virtualenv.py
-rwx------+ 1 Paul Kein  2809 Jun 22 20:05 pyenv-virtualenvs
~~~

Each of the Linux Bash scripts has finally a .BAT file counterpart, which does the job in Windows.

If the job is too complicated for .CMD, an additional .PY script is in place to bypass the painful failure risks using the Python version, which is globally installed in 'pyenv'.

### Creating Python Virtual Environment

'pyenv' command to create Python virtual environment:
~~~{.cmd}
pyenv virtualenv 3.12.10 cinema_5
~~~

This batch job has the following arguments:
1. The Python complete version number or a shorter version number of the installed Python language (e.g. 3.12.10, 3.12, etc.).
2. The short name of the project, which will get its Python Virtual Environment (e.g. 'cinema_5').
3. Optional: to set the local project properties (e.g. file '.python-version' in the project main folder). 

The batch job structures into the following steps:

1. Modify the PATH environment variable:
~~~{.cmd}
@echo off
set /a RC=0
setlocal
set OLD_PATH=%PATH%
set PATH=%PYENV_ROOT%versions\%~1;%PATH% 
~~~

2. Install the package "virtualenv":
~~~{.cmd}
# Check if "virtualenv" is installed
pip list
# If not, instruct the user how to install: 
#   > pip install virtualenv
goto cleanup
~~~

3. Make and change directories:
~~~{.cmd}
cd "%PYENV_ROOT%versions\%~1
ls -l
mkdir envs
cd envs
mkdir "%~2"
~~~

4. Check where Python is located:
~~~{.cmd}
where python
~~~
Output:
~~~
C:\Users\Paul\.pyenv\pyenv-win\versions\3.12.10\python.exe
C:\Users\Paul\.pyenv\pyenv-win\shims\python
C:\Users\Paul\.pyenv\pyenv-win\shims\python.bat
C:\cygwin64\bin\python
C:\Program Files\KiCad\8.0\bin\python.exe
C:\Program Files\Inkscape\bin\python.exe
C:\Users\Paul\AppData\Local\Microsoft\WindowsApps\python.exe
C:\Program Files\KiCad\bin\python.exe
~~~
~~~
C:\Users\Paul\.pyenv\pyenv-win\plugins\pyenv-virtualenv\bin>where python
~~~
5. Create the Python Virtual Environment:
~~~{.cmd}
python -m venv "%PYENV_ROOT%versions\%~1\envs\%~2"
echo %errorlevel%
~~~
Output:
~~~
0
~~~

6. Create symlink in 'versions' folder:
~~~{.cmd}
mklink /J "%PYENV_ROOT%versions\%~2" "%PYENV_ROOT%versions\%~1\envs\%~2"
~~~

7. Test & Upgrade:
~~~{.cmd}
ls -l "%PYENV_ROOT%versions\%~1\envs\%~2"
path
where activate
"%PYENV_ROOT%versions\%~1\envs\%~2\Scripts\activate.bat"
path
cd "%PYENV_ROOT%plugins\pyenv-virtualenv"
where pip
pip list
python -m pip install --upgrade pip
pip install pip-check
pip install pip-review
pip install psutil
pip-check
pip freeze > requirements.txt
cat requirements.txt
where python
python
>>> import psutil
>>> psutil.cpu_freq()
>>> quit()
deactivate
path
cd "%USERPROFILE%\eclipse-workspace\cinema_5"
~~~

8. Finally, clean-up the PATH environment variable:
~~~{.cmd}
:cleanup
set PATH=%OLD_PATH%
exit
~~~

## Patching "pyenv.bat"

### Overview

In any case a user installs 'pyenv-virtualenv', it automatically selects a patch pf 'pyenv.bat' for a known "pyenv" version.

But nobody knows what the future holds.

Until the author/responsible for 'pyenv' overtakes the patch code and its maintenance into the "pyenv.bat", we must check/adopt the future 'pyenv-virtualenv'-compatible patches. 

Afterward, you must publish a new 'pyenv-virtualenv' version, which includes that patch.

### Engineer a New Version

E.g. if the user installs a new 'pyenv' version and afterward the actual 'pyenv-virtualenv' plugin, then he will get an error message. 

In addition, the new original 'pyenv.bat' will be copied to 'patch\\pyenv_ori_{new_version}' in this directory:
~~~
%PYENV_ROOT%plugins\pyenv-virtualenv\patch
~~~
Content:
~~~
pyenv_ori_3.1.1.bat
pyenv_ori_{new_version}.bat
pyenv_ptc_3.1.1.bat
~~~

> NOTE: "\*ori\*.bat" is the original file from "pyenv". Do not edit this file in any case.

Follow to this approach to adopt 'pyenv-virtualenv':
1. Analyse in Notepad++ (compare plugin needed), what has changed in the new version.
2. Identify and move the patches code lines from the actual patch to the new patch file 'pyenv_ptc_{new_version}' to its new locations.
3. Develop the new patch.
4. Copy the resulting new patch file to '%PYENV_ROOT%\\plugins\\pyenv-virtualenv\\shims\\pyenv.bat'. 
5. Test the new patch in minimum with these most import commands:
  * pyenv virtualenvs
  * pyenv venv-list
  * pyenv virtualenv {version} {name}
  * pyenv venv-new {version} {name}
  * activate (inside a test project)
  * deactivate
  * activate {name}
  * deactivate
  * activate {version} {name}
  * deactivate
6. Adopt and test the 'pyenv-virtualenv" 'install.bat' and its sub processes.
7. Adopt and check the 'pyenv-virtualenv' change log.
8. Adopt, compile and test the 'pyenv-virtualenv' documentation.
9. Create/adopt/build the new 'pyenv-virtualenv' package (see PyPI documentation).
10. Publish the new 'pyenv-virtualenv' package on PyPI.

## Working Techniques

Programming in Windows Command Line Interface, Windows Installer Scripts and Pascal is a fast, easy and less challenging job.

To realize this web application and its scripts, the following specialized working techniques have been used to reach the goal.

### Entropy Reduction

Entropy is the greatest enemy of the developing process.

Every disorder of the natural order of things is creating chaos, which results in malfunctions, which could resist many hours of analysis.

The solution is to reduce the entropy in the code, wherever we intuitively feel to detect it.

This strategy immediately results in working code and a breakthrough, which could save the whole project.

To maximize the success of this strategy, it is wise to holistically focus and reduce entropy in these realms too:
  * developer's personal lifestyle, life-long education, mental and physical health,
  * working conditions,
  * environmental conditions,
  * collective constraints,
  * economic constraints.

> NOTE: Having more attitudes, compulsions, and limitations of any kind increases entropy. This is definitely counterproductive and leads into more chaos. Instead, create a space for nourished evolution of insights and feelings, and let successful things happen step by step.

### Python Virtual Environment

> NOTE: THIS. IS. ESSENTIAL.

If you develop multiple Python applications on Windows it is essential to use these tool and its plugin:
* 'pyenv' for Windows 
  * 'pyenv-virtualenv' for Windows. 

Otherwise, you will create an entropic valley of tears.

### Using Templates

To avoid obsolete recurring workload, it is a good idea to use templates.

In this project the PyCharm IDE is capable to use file and code templates. See 'Tooling' / 'PyCharm Community Edition'.

Templates are accelerating the coding process.

### Frameworks

To build a stable and reliable application, it is essential to use state-of-the-art development frameworks. 

This reduces the known wild growth of multiple and incompatible constructional entropy, which could jeopardize the hole project.

### Badges

A Badge represents a newly established form of a link, which has a unique modern  look and feel. 

Opposite to linked text, it is easier operate on touch surfaces/interfaces e.g. on smartphones or tablets:

Examples:

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/#table_of_contents)

[![license](https://img.shields.io/badge/License-GPL%203.0-20A040)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/LICENSE)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/CODE_OF_CONDUCT.md)

![pypi](https://img.shields.io/badge/PyPI-1.24-2040A0)
![python](https://img.shields.io/badge/Python-3.6%20|%203.8%20|%203.9%20|%203.10%20|%203.11%20|%203.12%20|%203.13-C0C040)

In this project badges are used in the main README.md on GitHub to ease and accelerate navigating through the document with a minimum of scrolling.

Another purposes are to give short information or to link to other websites. 

Many thanks to the people of the 'shields.io' organization, who give the members of the worldwide open source community the opportunity to use this service for free for their projects. 

### Colored Output to Console

To make console application logging more readable, it is a good idea to colorize the logging highlights.

E.g. in the Python coloredlogs, customized in my own CLI framework:

  * CRITICAL: bright red
  * ERROR: red
  * SUCCESS: bright green
  * WARNING: yellow
  * NOTICE: bright white
  * INFO: bright white
  * VERBOSE: blue
  * DEBUG: green
  * SPAM: dimmed gray

The ANSI (American National Standards Institute) color codes are a widely adopted system used to control the color output of text in terminal and console environments. 

Originally designed for Unix systems, these codes allow developers and users to add color to command-line interfaces (CLIs), making output more readable and visually appealing. 

ANSI codes are supported by most modern terminals, allowing for easy customization of text color, background color, and text styles (like bold or underline).

The colored text output control character sequences are available Linux, macOS and Windows command line interface (CLI): 

![colored_log_specification_windows](./images/colored_log_specification_windows.png "ANSI Colored Log Specification")

See the <a href="https://gist.github.com/chouhan-rahul/011f69b3117734ae7dd3a8c281dde0d5" rel="noopener noreferrer" target="_blank">ANSI Color Codes: A Comprehensive Guide</a> for details.

#### Linux BASH

The ESC character is given in octal code (\\033). Example:

~~~
\033[92mDONE (RC = 0).\033[0m"
~~~

Code example to log a colored log to console:

~~~{.bash}
# "echo" colored
RC=0
echo -e "\033[92mImport successfully completed (RC = $RC).\033[0m"
~~~

> NOTE: The '\\033' sub string codes are the ESC characters.

#### Windows CMD

~~~
echo [92mDONE (RC = 0).[0m
~~~

Code example to log a colored log to console:

~~~{.cmd}
REM "echo" colored
set /a rc=0
echo [92mImport successfully completed (RC = %RC%).[0m
~~~

> NOTE: The '' are symbolizing the ESC characters. The ESC key on the keyboard does not work. Instead, type these by pressing Alt-027 in Notepad++ or other capable code editors.

> NOTE: To view the ESC characters in the Notepad++ code editor, set 'Menu' / 'View' / 'Show all characters'.

#### Windows PowerShell

~~~
Write-Host "$([char]27)[92mDONE (RC = 0).$([char]27)[0m"
~~~

Code example to log a colored log to console:

~~~{.ps1}
# "echo" colored
$rc = 0
Write-Host "$([char]27)[92mImport successfully completed (RC = $rc).$([char]27)[0m"
~~~

> NOTE: The '$([char]27)' sub string codes are the ESC characters. 

#### Python

~~~{.py}
# Reinitialize console output to avoid the missing color problem
import os
os.system('')
# "print" colored
rc = 0
print(f'\x1b[92mImport successfully completed (RC = {rc}).\x1b[0m')
~~~

> NOTE: The '\\x1b' sub string codes are the ESC characters.

> NOTE: For multi-platform code in Python, it is more efficient to use the specific objects in the e.g. the libraries 'colorama' or 'coloredlogs' to explicitly colorize output text or to colorize the complete logging to console.

### Cross Platform Development

In computing, cross-platform software (also called multi-platform software, platform-agnostic software, or platform-independent software) is computer software that is designed to work in several computing platforms. Some cross-platform software requires a separate build for each platform, but some can be directly run on any platform without special preparation, being written in an interpreted language or compiled to portable byte code for which the interpreters or run-time packages are common or standard components of all supported platforms.

For example, a cross-platform application may run on Linux, macOS and Microsoft Windows. Cross-platform software may run on many platforms, or as few as two.

In this project the Python scripts are coded in this way. The advantage is that the code or parts of the code could run on supported platforms Linux, macOS and Windows.

### Time-Consuming Procedure Surveillance

If a script is operating slow processes or time-consuming procedures, it is essential to inform the user about the progress. Otherwise, the user could think, that the program crashed.

In that case a sub thread must be created to surveillance the long-running procedure or process in parallel.

In this project, we use these methods to inform the user inside that thread:
  * Continuous log text lines with information in the command line.
  * Continuous print a progress bar in the command line, if necessary.
  * Display a temporary waiting prompt in the command line, if necessary.

E.g. a progress bar in Python could be printed in this way:
~~~{*.py}
	@staticmethod
	def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', color='green', print_end="\r") -> None:
		percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
		filled_length = math.ceil(length * iteration / total)
		bar = fill * filled_length + '-' * (length - filled_length)
		begin_color = eval(f'colorama.Fore.{color.upper()}')
		end_color = colorama.Style.RESET_ALL
		print(f'\r{prefix} |{begin_color}{bar}{end_color}| {percent} % {suffix}', end=print_end)

~~~

This simple progress bar print routine can be translated into .CMD, .SH, etc. languages to use within other platforms on command line console.

## Design

### Scripts

The whole project is automated by the implemented scripts.

See details in the commented source code of the Windows command line scripts and Python scripts:
  * Packages
  * Classes
  * Files

See at the bottom of the navigation panel on the left.

> NOTE: For Windows Command Line scripts (.BAT) and (.PS1) there are currently no Doxygen programming language plugins available. For these files I documented the code inside using comments, which follow the common Doxygen syntax. See the comments inside the code of these files.


--- END OF DOCUMENT ---
