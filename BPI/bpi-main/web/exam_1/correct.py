#!/usr/bin/env python3

"""This program is used to correct the exam_1"""

from abc import ABC, abstractmethod
import argparse
import contextlib
import dataclasses
import importlib.util
import io
import itertools
import os
import re
import subprocess
import sys
import traceback
import typing
import unicodedata

# On utilise la version corrigée comme référence
# pour les tests.
import combinaisons_corrigee


def parse_arguments():
    """Manage arguments."""
    parser = argparse.ArgumentParser(description="Correction automatique.")
    parser.add_argument(
        "--verbose", "-v", action=argparse.BooleanOptionalAction, default=False
    )
    return parser.parse_args()


@dataclasses.dataclass(frozen=True)
class TestResult:
    "A test result has a nb_tests_ok and a list of messages"
    nb_tests_ok: int
    messages: str


NO_RESULT = TestResult(0, "NO_RESULT")


def strip_accents(string: str) -> str:
    """Remove all accents in s"""
    return "".join(
        c
        for c in unicodedata.normalize("NFD", string)
        if unicodedata.category(c) != "Mn"
    )


class AbstractTest(ABC):
    """Abstract base class for all tests"""

    def __init__(self, name: str, nb_tests: int, cwd: str):
        self.name: str = name
        self.nb_tests: int = nb_tests
        self.result: TestResult = NO_RESULT
        self.cwd: str = cwd

    def run(self, verbose):
        """run the test and print the result

        Fail the test if any exception is thrown
        """
        # pylint: disable=broad-except
        try:
            self.result = self.run_test()
        except Exception as exc:
            messages = [
                "Exception de type " + type(exc).__name__ + " imprévue lancée",
            ]
            if verbose:
                exc_io_s = io.StringIO()
                traceback.print_exception(
                    type(exc), exc, exc.__traceback__, file=exc_io_s
                )
                exc_io_s.getvalue()
                messages.append(exc_io_s.getvalue())
            self.result = TestResult(nb_tests_ok=0, messages=messages)
        print(self.name)
        if self.result.messages:
            for message in self.result.messages:
                print(" ", message)
        print(f"  Nombre de tests OK = {self.result.nb_tests_ok}/{self.nb_tests}")

    def import_combinaisons(self):
        """Import the combinaisons module in the working directory of self."""
        prog_file_path = os.path.join(self.cwd, "combinaisons.py")
        spec = importlib.util.spec_from_file_location("combinaisons", prog_file_path)
        combinaisons = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(combinaisons)
        return combinaisons

    @abstractmethod
    def run_test(self) -> TestResult:
        """run the test and return a TestResult"""


class TestTeste(AbstractTest):
    """Test that the `teste` fonction is correct"""

    def __init__(self, cwd: str):
        super().__init__(
            name="Implémentation de la fonction `teste()`",
            nb_tests=6,
            cwd=cwd,
        )

    @typing.no_type_check
    def run_test(self) -> TestResult:
        """Check all the prints of teste.

        First import combinaisons.py as a module and call its teste function while :
            - all other functions are replaced by the correction ones
            - redirecting stdout to record it

        Then look for correct outputs in the recorded stdout
        """

        # Import combinaisons and replace all functions except `teste`
        combinaisons = self.import_combinaisons()

        # Run `teste` while redirecting stdout
        out = io.StringIO()
        with contextlib.redirect_stdout(out):

            # If so that can be called from correct_all.py too
            if len(sys.argv) == 1:
                sys.argv.append("input.txt")
            else:
                sys.argv[1] = "input.txt"

            # Save tested module functions and replace them by the
            # correction's ones.
            old_recupere_combinaisons_2 = combinaisons.recupere_combinaisons_2
            old_recupere_parametres = combinaisons.recupere_parametres
            old_recupere_combinaisons = combinaisons.recupere_combinaisons
            combinaisons.recupere_combinaisons_2 = (
                combinaisons_corrigee.recupere_combinaisons_2
            )
            combinaisons.recupere_parametres = combinaisons_corrigee.recupere_parametres
            combinaisons.recupere_combinaisons = (
                combinaisons_corrigee.recupere_combinaisons
            )

            # Run `teste` function of tested module and gets its output
            combinaisons.teste()
            out = out.getvalue()

            # Restore saved tested module functions (is this really needed ?)
            combinaisons.recupere_combinaisons_2 = old_recupere_combinaisons_2
            combinaisons.recupere_parametres = old_recupere_parametres
            combinaisons.recupere_combinaisons = old_recupere_combinaisons

        # Then we look for the human answer of 2-combinaisons on 'ABCD'
        nb_tests_ok = 0
        lines = list(
            " ".join(strip_accents(l).lower().split()) for l in out.split("\n")
        )
        messages = []
        if all(
            "".join(combin) in lines for combin in itertools.combinations("abcd", r=2)
        ):
            nb_tests_ok += 1
            messages.append(
                "Test 1 OK : les résultats calculés dans ta tête "
                "pour la sequence 'ABCD' et k=2 sont corrects"
            )
        else:
            messages.append(
                "Test 1 KO : les résultats calculés dans ta tête "
                "pour la sequence 'ABCD' et k=2 sont incorrects"
            )

        # Then we check that recupere_combinaisons_2 is properly called and its
        # result properly displayed
        if all(str(combin) in lines for combin in itertools.combinations("abcd", r=2)):
            nb_tests_ok += 1
            messages.append(
                "Test 2 OK : appel et affichage du résultat de "
                "recupere_combinaisons_2('ABCD') correct"
            )
        else:
            messages.append(
                "Test 2 KO : appel et affichage du résultat de "
                "recupere_combinaisons_2('ABCD') incorrect"
            )

        # Then we look for the human answer of 3-combinaisons on [0, 1, 2, 3, 4]
        if all(
            "".join(str(elem) for elem in combin) in lines
            for combin in itertools.combinations([0, 1, 2, 3, 4], r=3)
        ):
            nb_tests_ok += 1
            messages.append(
                "Test 3 OK : les résultats calculés dans ta tête "
                "pour la sequence [0, 1, 2, 3, 4] et k=3 sont corrects"
            )
        else:
            messages.append(
                "Test 3 KO : les résultats calculés dans ta tête "
                "pour la sequence [0, 1, 2, 3, 4] et k=3 sont incorrects"
            )

        # Then we check that recupere_combinaisons is properly called and its
        # result properly displayed
        if all(
            str(combin) in lines
            for combin in itertools.combinations([0, 1, 2, 3, 4], r=3)
        ):
            nb_tests_ok += 1
            messages.append(
                "Test 4 OK : appel et affichage du résultat de "
                "recupere_combinaisons([0, 1, 2, 3, 4], 3) correct"
            )
        else:
            messages.append(
                "Test 4 KO : appel et affichage du résultat de "
                "recupere_combinaisons([0, 1, 2, 3, 4], 3) incorrect"
            )

        # Then we check that recupere_parametres is properly called and the
        # result is properly displayed
        if all(
            expected in lines for expected in ("['a', 'b', 'c', 'd', 'e', 'f']", "3")
        ):
            nb_tests_ok += 1
            messages.append(
                "Test 5 OK : appel et affichage du résultat de recupere_parametres correct"
            )
        else:
            messages.append(
                "Test 5 KO : appel et affichage du résultat de recupere_parametres incorrect"
            )

        # Then we check that recupere_parametres and recupere_combinaisons are
        # properly called and the result properly used and displayed
        if all(
            str(combin) in lines for combin in itertools.combinations("abcdef", r=3)
        ):
            nb_tests_ok += 1
            messages.append(
                "Test 6 OK : appel et affichage du résultat de recupere_combinaisons "
                "sur les parametres dans le fichier correct"
            )
        else:
            messages.append(
                "Test 6 KO : appel et affichage du résultat de recupere_combinaisons "
                "sur les parametres dans le fichier incorrect"
            )

        return TestResult(nb_tests_ok, messages)


class TestRecupereParams(AbstractTest):
    """Test that the `recupere_parametres` function is correct"""

    def __init__(self, cwd: str):
        super().__init__(
            name="Implémentation de la fonction `recupere_parametres()`",
            nb_tests=2,
            cwd=cwd,
        )

    def run_test(self):
        """Call the `recupere_parametres` function and check its result"""

        # Call its recupere_parametres function
        combinaisons = self.import_combinaisons()
        try:
            seq, k = combinaisons.recupere_parametres("input.txt")
        except TypeError:
            seq, k = None, None
        seq_prof, k_prof = combinaisons_corrigee.recupere_parametres("input.txt")

        # Is the sequence ok
        messages = []
        nb_tests_ok = 0
        if seq and list(seq) == list(seq_prof):
            nb_tests_ok += 1
            messages.append(f"Test 1 OK : séquence renvoyée correcte : {seq}")
        else:
            messages.append(
                f"Test 1 KO : séquence renvoyée incorrecte : {seq}, "
                f"au lieu de {list(seq_prof)}"
            )

        # Is the k ok
        if k == k_prof:
            nb_tests_ok += 1
            messages.append(f"Test 2 OK : k renvoyé correct : {k}")
        else:
            messages.append(
                f"Test 2 KO : k renvoyé incorrect : {k}, au lieu de {k_prof}"
            )

        return TestResult(nb_tests_ok, messages)


class TestRecupereCombinaison2(AbstractTest):
    """Test that the `recupere_combinaisons_2` fonction is correct"""

    def __init__(self, cwd: str):
        super().__init__(
            name="Implémentation de la fonction `recupere_combinaisons_2`",
            nb_tests=2,
            cwd=cwd,
        )

    def run_test(self):
        """Call the `recupere_combinaisons_2` function and check its result"""

        # Is the call on "ABCD" correct
        combinaisons = self.import_combinaisons()
        combins = combinaisons.recupere_combinaisons_2("ABCD")
        combins_corrige = combinaisons_corrigee.recupere_combinaisons_2("ABCD")
        messages = []
        nb_tests_ok = 0
        if combins and set(combins) == set(combins_corrige):
            nb_tests_ok += 1
            messages.append(f"Test 1 OK : list renvoyée correcte pour ABCD : {combins}")
        else:
            messages.append(
                f"Test 1 KO : list renvoyée incorrecte pour ABCD : {combins}, "
                f"au lieu de {combins_corrige}"
            )

        # Is the call on [0, 1, 2, 3, 4] correct
        combins = combinaisons.recupere_combinaisons_2([0, 1, 2, 3, 4])
        combins_corrige = combinaisons_corrigee.recupere_combinaisons_2([0, 1, 2, 3, 4])
        if combins and set(combins) == set(combins_corrige):
            nb_tests_ok += 1
            messages.append(
                f"Test 2 OK : list renvoyée correcte pour [0, 1, 2, 3, 4] : {combins}"
            )
        else:
            messages.append(
                f"Test 2 KO : list renvoyée incorrecte pour [0, 1, 2, 3, 4] : {combins}, "
                f"au lieu de {combins_corrige}"
            )

        return TestResult(nb_tests_ok, messages)


class TestRenverse(AbstractTest):
    """Test that the `renverse` fonction is correct"""

    def __init__(self, cwd: str):
        super().__init__(
            name="Implémentation de la fonction `renverse`",
            nb_tests=3,
            cwd=cwd,
        )

    def run_test(self):
        """Call the `recupere_combinaisons_2` function and check its result"""

        # Is the call on [] correct
        combinaisons = self.import_combinaisons()
        renv = combinaisons.renverse([])
        renv_corrige = combinaisons_corrigee.renverse([])
        messages = []
        nb_tests_ok = 0
        if renv == renv_corrige:
            nb_tests_ok += 1
            messages.append(f"Test 1 OK : list renvoyée pour [] correcte : {renv}")
        else:
            messages.append(
                f"Test 1 KO : list renvoyée pour [] incorrecte : {renv}, au lieu de {renv_corrige}"
            )

        # Is the call on [4, 3, 2, 1, 0] correct
        renv = combinaisons.renverse([4, 3, 2, 1, 0])
        renv_corrige = combinaisons_corrigee.renverse([4, 3, 2, 1, 0])
        if renv == renv_corrige:
            nb_tests_ok += 1
            messages.append(
                f"Test 2 OK : list renvoyée pour [4, 3, 2, 1, 0] correcte : {renv}"
            )
        else:
            messages.append(
                f"Test 2 KO : list renvoyée pour [4, 3, 2, 1, 0] incorrecte : {renv}, "
                f"au lieu de {renv_corrige}"
            )

        # Is the call on [0, 1, 2, 3, 4] correct
        renv = combinaisons.renverse([0, 1, 2, 3, 4])
        renv_corrige = combinaisons_corrigee.renverse([0, 1, 2, 3, 4])
        if renv == renv_corrige:
            nb_tests_ok += 1
            messages.append(
                f"Test 3 OK : list renvoyée pour [0, 1, 2, 3, 4] correcte : {renv}"
            )
        else:
            messages.append(
                f"Test 3 KO : list renvoyée pour [0, 1, 2, 3, 4] incorrecte : {renv}, "
                f"au lieu de {renv_corrige}"
            )

        return TestResult(nb_tests_ok, messages)


class TestRecupereCombinaison(AbstractTest):
    """Test that the `recupere_combinaisons` fonction is correct"""

    def __init__(self, cwd: str):
        super().__init__(
            name="Implémentation de la fonction `recupere_combinaisons`",
            nb_tests=2,
            cwd=cwd,
        )

    def run_test(self):
        """Call the `recupere_combinaisons` function and check its result"""
        # Import combinaisons.py as a module
        combinaisons = self.import_combinaisons()

        # Is the call on "ABCD" and k=2 correct
        combins = combinaisons.recupere_combinaisons("ABCD", 2)
        combins_corrige = combinaisons_corrigee.recupere_combinaisons("ABCD", 2)
        messages = []
        nb_tests_ok = 0
        if combins and set(combins) == set(combins_corrige):
            nb_tests_ok += 1
            messages.append(
                f"Test 1 OK : list renvoyée pour 'ABCD' et 2 correcte : {combins}"
            )
        else:
            messages.append(
                f"Test 1 KO : list renvoyée pour 'ABCD' et 2 incorrecte : {combins}, au lieu de {combins_corrige}"
            )

        # Is the call on [0, 1, 2, 3, 4] correct
        combins = combinaisons.recupere_combinaisons([0, 1, 2, 3, 4], 3)
        combins_corrige = combinaisons_corrigee.recupere_combinaisons(
            [0, 1, 2, 3, 4], 3
        )
        if combins and set(combins) == set(combins_corrige):
            nb_tests_ok += 1
            messages.append(
                f"Test 2 OK : list renvoyée pour [0, 1, 2, 3, 4] et 3 correcte : {combins}"
            )

        else:
            messages.append(
                f"Test 2 KO : list renvoyée pour [0, 1, 2, 3, 4] et 3 incorrecte : {combins}, "
                f"au lieu de {combins_corrige}"
            )

        return TestResult(nb_tests_ok, messages)


class TestComplexiteRecupereCombinaison(AbstractTest):
    """Test nothing."""

    def __init__(self, cwd: str):
        super().__init__(
            name="Complexité de la fonction `recupere_combinaisons`",
            nb_tests=1,
            cwd=cwd,
        )

    def run_test(self):
        """Do nothing"""
        return TestResult(
            1,
            (
                "Test 1 OK : c'est pas évident à tester, donc tu as juste "
                "quelque soit ta réponse, sympa non ?",
            ),
        )


class TestPylint(AbstractTest):
    """Test that pylint does not complains too much on the code."""

    def __init__(self, cwd: str):
        super().__init__(
            name="Que dit pylint sur ton fichier `combinaisons.py` ?",
            nb_tests=1,
            cwd=cwd,
        )

    def run_test(self):
        """Run pylint on combinaisons.py"""
        cmd = ["pylint", "combinaisons.py"]
        subprocess_result = subprocess.run(cmd, stdout=subprocess.PIPE, check=False)
        score_regexp = re.compile(r".*Your code has been rated at (.*)/10 ")
        score = None
        for line in subprocess_result.stdout.decode().split("\n"):
            score_match = score_regexp.search(line.strip())
            if score_match:
                score = float(score_match.group(1))
        if score:
            if score < 5:
                nb_tests_ok = 0
                message = ("Test 1 KO : score de pylint compris entre 0 et 5 ---> -2",)
            elif 5 <= score < 8:
                nb_tests_ok = 0
                message = ("Test 1 KO : score de pylint compris entre 5 et 8 ---> -1",)
            else:
                nb_tests_ok = 1
                message = (
                    "Test 1 OK : score de pylint compris entre 8 et 10 ---> pas de malus",
                )
        else:
            nb_tests_ok = 1
            message = (
                "Test 1 OK : t'as de la chance, on a pas réussi à avoir ton score au près de pylint !",
            )
        return TestResult(nb_tests_ok, message)


def check_for_combinaisons_file(cwd: str):
    """Return true if input is used"""
    return os.path.isfile(os.path.join(cwd, "combinaisons.py"))


def check_for_func_usage(cwd: str, func_name: str):
    """Return true if the given function is called"""
    with open(
        os.path.join(cwd, "combinaisons.py"), "r", encoding="utf8"
    ) as source_file:
        for line in source_file:
            if f"{func_name}(" in line and not line.strip().startswith("#"):
                return True
    return False


def check_for_input_usage(cwd: str):
    """Return true if input is used"""
    return check_for_func_usage(cwd, "input")


def check_for_exit_usage(cwd: str):
    """Return true if exit is used"""
    return check_for_func_usage(cwd, "exit")


def correct(cwd: str):
    """run all the tests if we can"""

    args = parse_arguments()

    tests = (
        TestTeste(cwd),
        TestRecupereParams(cwd),
        TestRecupereCombinaison2(cwd),
        TestRenverse(cwd),
        TestRecupereCombinaison(cwd),
        TestComplexiteRecupereCombinaison(cwd),
        TestPylint(cwd),
    )
    nb_tests_total = sum(t.nb_tests for t in tests)

    cwd = os.path.abspath(cwd)
    if not check_for_combinaisons_file(cwd):
        message = (
            "je ne peux pas corriger ton travail car il n'y a pas de fichier "
            "combinaisons.py dans ton dossier exam."
        )
        print(message)
        return "N/A", nb_tests_total, message
    if check_for_input_usage(cwd):
        message = (
            "je ne peux pas corriger ton travail car tu utilises la fonction input, "
            "supprime toutes les utilisations d'input et relance la correction."
        )
        print(message)
        return "N/A", nb_tests_total, message
    if check_for_exit_usage(cwd):
        message = (
            "je ne peux pas corriger ton travail car tu utilises la fonction exit, "
            "supprime toutes les utilisations d'exit et relance la correction."
        )
        print(message)
        return "N/A", nb_tests_total, message

    nb_tests_ok = 0
    for test in tests:
        test.run(args.verbose)
        nb_tests_ok += test.result.nb_tests_ok
        if "SyntaxError" in test.result.messages:
            message = (
                "je ne peux pas corriger ton travail car il y a une erreur "
                "de syntaxe dans ton programme."
            )
            print(message)
            return "N/A", nb_tests_total, message
    print(f"Nombre de tests OK = {nb_tests_ok}/{nb_tests_total}")
    return nb_tests_ok, nb_tests_total, ""


if __name__ == "__main__":
    correct(".")
