function RawBlock(el)
  if el.format == 'tex' and el.text == '\\sectionbreak' then
    return pandoc.RawBlock('openxml',
      [[
      <w:p>
        <w:pPr>
          <w:sectPr>
            <w:type w:val="nextPage"/>
          </w:sectPr>
        </w:pPr>
      </w:p>
      ]]
    )
  end
end
