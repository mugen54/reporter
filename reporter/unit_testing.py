from unittest.mock import patch
import report_filler


@patch("report_filler.ReportFiller")
def test(MockClass1):

    report_filler.ReportFiller()

    assert MockClass1 is report_filler.ReportFiller

    assert MockClass1.called


test()
