import pystdf

# 打开STDF文件
with open('example.stdf', 'rb') as stdf_file:
    # 创建STDF解析器对象
    stdf = pystdf.STDFFile(stdf_file)

    # 创建CSV文件
    with open('example.csv', 'w', newline='') as csv_file:
        # 获取记录类型码列表
        record_types = stdf.record_types

        # 写入表头
        csv_file.write(','.join(record_types) + '\n')

        # 逐条解析记录并写入CSV文件
        for record in stdf:
            # 解析记录类型码和数据
            record_type = record.record_type
            record_data = record.to_dict()

            # 将数据转换为CSV格式并写入文件
            csv_row = ','.join(str(record_data.get(field, '')) for field in record_types)
            csv_file.write(csv_row + '\n')
