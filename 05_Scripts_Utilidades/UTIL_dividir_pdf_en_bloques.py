import PyPDF2
import os

pdf_path = r'D:\Users\cra\Desktop\Sec+\SecPlus_SY0-701_FUSIONADO.pdf'
output_dir = r'D:\Users\cra\Desktop\Sec+\bloques_pdf'

# Leer PDF
with open(pdf_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    total_pages = len(pdf_reader.pages)

    print(f"Total de páginas: {total_pages}")

    # Dividir en bloques de 10 páginas
    pages_per_block = 10
    num_blocks = (total_pages + pages_per_block - 1) // pages_per_block

    for block_num in range(num_blocks):
        start_page = block_num * pages_per_block
        end_page = min(start_page + pages_per_block, total_pages)

        # Crear nuevo PDF para este bloque
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(start_page, end_page):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Guardar bloque
        output_filename = os.path.join(output_dir, f'SecPlus_bloque_{block_num+1:02d}.pdf')
        with open(output_filename, 'wb') as output_file:
            pdf_writer.write(output_file)

        print(f"[OK] Bloque {block_num+1:02d}: paginas {start_page+1}-{end_page} -> {os.path.basename(output_filename)}")

print(f"\n[COMPLETADO] {num_blocks} bloques creados en {output_dir}")
