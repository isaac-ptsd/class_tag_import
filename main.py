# classTag tool
from __future__ import print_function
from gooey import Gooey, GooeyParser
import pandas as pd
import os.path

#  must create one .csv file per school


@Gooey(program_name="ClassTag Tool")
def main():
    # do stuff
    parser = GooeyParser(description='PowerSchool export to Dovestone/Active Directory import file')
    parser.add_argument('Save_Location',
                        action='store',
                        widget='DirChooser',
                        help="Output directory to save csv file")
    parser.add_argument('File_Name',
                        action='store',
                        help="Save as:")  # output file name
    parser.add_argument('Student_File',
                        action='store',
                        widget='FileChooser',
                        help="Select a PowerSchool export (.csv)")  # file read-in
    parser.add_argument('Staff_File',
                        action='store',
                        widget='FileChooser',
                        help="Select a PowerSchool export (.csv)")  # file read-in
    parser.add_argument('Contact_File',
                        action='store',
                        widget='FileChooser',
                        help="Select a PowerSchool export (.csv)")  # file read-in

    user_inputs = vars(parser.parse_args())
    output_dir = user_inputs['Save_Location']
    file_name = user_inputs['File_Name']
    student_csv_in = user_inputs['Student_File']
    staff_csv_in = user_inputs['Staff_File']
    contact_csv_in = user_inputs['Contact_File']
    in_student_df = pd.read_csv(student_csv_in, encoding='latin1')
    in_staff_df = pd.read_csv(staff_csv_in, encoding='latin1')
    in_contact_df = pd.read_csv(contact_csv_in, encoding='latin1')
    out_df = pd.DataFrame(columns=['sourcedId',
                                   'role',
                                   'givenName',
                                   'familyName',
                                   'email',
                                   'sms',
                                   'phone',
                                   'agentSourcedIds',
                                   'language'])
    # write all student and staff data into out_df
    out_df = out_df.append(in_student_df, ignore_index=True)
    out_df = out_df.append(in_student_df, ignore_index=True)


if __name__ == '__main__':
    main()
