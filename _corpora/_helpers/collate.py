from pathlib import Path

def collate_by_filetype(data_dir, extension, outfile):

    in_files = Path(data_dir).glob(f'*.{extension}')

    with open(outfile, 'wb') as f_out:
        for f in in_files:
            with open(f, "rb") as f_in:
                f_out.write(f_in.read())
